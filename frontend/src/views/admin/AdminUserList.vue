<template>
  <div class="user-list-container">
    <h2>User Management</h2>

    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Username</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in paginatedUsers" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.username }}</td>
          <td>
            <button class="admin-btn" @click="setAdmin(user.id)">Set as Admin</button>
            <button class="delete-btn" @click="deleteUser(user.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- ✅ 分页按钮 -->
    <div class="pagination">
      <button class="page-btn" @click="prevPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button class="page-btn" @click="nextPage" :disabled="currentPage === totalPages">Next</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import axios from "axios";
import { post } from "@/net";

// ✅ 存储用户数据
const users = ref([]);
const currentPage = ref(1);
const pageSize = 8;  // ✅ 每页显示 n 个用户

// ✅ 获取 JWT 令牌
const getAuthHeaders = () => {
  const token = localStorage.getItem("accessToken");
  return {
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
  };
};

// ✅ 1. 获取所有普通用户
const fetchUsers =  () => {
  try {
    post('/api/post/user-list/',{},(res)=>{
      users.value=res
    })

    
  } catch (error) {
    console.error("Failed to fetch users:", error.response ? error.response.data : error);
  }
};

// ✅ 2. 计算分页数据
const totalPages = computed(() => Math.ceil(users.value.length / pageSize));

const paginatedUsers = computed(() => {
  const start = (currentPage.value - 1) * pageSize;
  return users.value.slice(start, start + pageSize);
});

// ✅ 3. 分页操作
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

// ✅ 4. 设置用户为管理员
const setAdmin = (userId) => {
  try {
    post('/api/post/set-admin/',{"user_id": userId},(res)=>{
      alert(res.message || "User has been set as admin.");
      fetchUsers();
    })
    
  } catch (error) {
    alert(error.response?.data?.error || "Failed to set admin.");
  }
};

// ✅ 5. 删除用户
const deleteUser =  (userId) => {
  try {
    post('/api/post/del-user/',{"user_id":userId},(res)=>{
      alert(res.message || "User deleted.");
      fetchUsers();
    })
    
  } catch (error) {
    alert(error.response?.data?.error || "Failed to delete user.");
  }
};

// ✅ 组件加载时获取用户列表
onMounted(fetchUsers);
</script>

<style scoped>
/* ✅ 让整个页面与主页风格匹配 */
.user-list-container {
  width: 80%;
  max-width: 1000px;
  height: 100vh;
  margin: auto;
  text-align: center;
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  margin-top: 30px;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}

/* ✅ 让 sidebar 保持一致 */
.sidebar {
  height: 50px !important;
  margin-top: 20px !important;
}

/* ✅ 优化表格，使其更贴合主页风格 */
table {
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
  
}

th, td {
  padding: 12px 16px;
  border-bottom: 1px solid #ddd;
  text-align: center;
}

th {
  background: #007bff;
  color: white;
  font-weight: bold;
}

tbody tr:hover {
  background: #f1f1f1;
}

/* ✅ 统一按钮样式 */
button {
  padding: 8px 12px;
  cursor: pointer;
  border-radius: 6px;
  font-size: 14px;
  font-weight: bold;
  transition: all 0.2s ease-in-out;
  border: none;
}

/* ✅ 管理员按钮 */
.admin-btn {
  background: #28a745;
  color: white;
}

.admin-btn:hover {
  background: #218838;
}

/* ✅ 删除按钮 */
.delete-btn {
  background: #dc3545;
  color: white;
  margin-left: 8px;
}

.delete-btn:hover {
  background: #c82333;
}

/* ✅ 分页按钮 */
.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 15px;
}

.page-btn {
  padding: 8px 16px;
  font-size: 14px;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background: #007bff;
  color: white;
}

.page-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}
</style>
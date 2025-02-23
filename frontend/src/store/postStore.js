import { defineStore } from "pinia";

export const usePostStore = defineStore("postStore", {
    state: () => ({
        selectedCategory: "All",
    }),
    actions: {
        setCategory(category) {
            this.selectedCategory = category;
        }
    }
});

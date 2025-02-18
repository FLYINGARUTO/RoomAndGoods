import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def upload_to_s3(file, bucket):
    """
    将文件上传到指定的 S3 存储桶。

    :param file: 文件
    :param bucket: S3 存储桶名称
    """


    object_name = 'uploads/'+file.name.split('/')[-1]

    # 创建 S3 客户端
    s3_client = boto3.client('s3')

    try:
        # 上传文件
        s3_client.upload_fileobj(file, bucket, object_name)
        print(f"✅ 文件 {object_name} 已成功上传到 S3 存储桶 {bucket}/{object_name}")
        return f'https://{bucket}.s3.eu-north-1.amazonaws.com/{object_name}'
    except FileNotFoundError:
        return "❌ 错误: 文件未找到"

    except NoCredentialsError:
        return "❌ 错误: AWS 凭证无效或未找到"
        
    except ClientError as e:
    
        return f"❌ 错误: {e}"
if __name__=='__main__':
    stt=upload_to_s3('/Users/flyingbuta/Desktop/UofG/s3_upload_test.py', 'my-it-bucket-glasgow', object_name=None)
    print(stt)
backend implementation is in "**myproject**" folder<br />
frontend implementation is in "**frontend**" folder


prepare the environment needed before you run it:<br />

python=3.10.9<br />
npm=10.9.2<br />
mysqlclient=2.0.3<br />
django=5.1.1<br />
django-cors-headers=4.7.0<br />
djangorestframework=3.15.2<br />
djangorestframework_simplejwt=5.4.0<br />
daphne=4.1.2<br />
channels=4.2.0<br />

pip install django djangorestframework<br />
pip install django-cors-headers<br />
pip install mysqlclient<br />
pip install channels<br />
pip install daphne<br />
pip install mysql-connector-python<br />
pip install djangorestframework-simplejwt<br />
<br />
**cd into frontend/ to run the following lines:**<br />
npm install vue axios vue-router<br />
npm install -D unplugin-vue-components unplugin-auto-import<br />
npm install pinia<br />


<br />

**the AWS database is temporarily shutdown**, so please do the following commands <br />
create a mysql database locally, tables are not necessary at this point<br />
configure your local database in **settings.py** first<br />
run the following code in the **myproject/**, the tables will be created according to definitions in **models.py**<br />
python manage.py makemigrations<br />
python manage.py migrate<br />
till this point, tables have been created accordingly.<br />
run the **GoodsAndRooms.sql** within your local database to inject the prepared data 

<br />
<br />

how to start the application:<br />


cd into myproject and run **daphne -b 0.0.0.0 -p 8000 myproject.asgi:application** to start the backend service <br />
cd into myproject and run **npm run dev -- --host 0.0.0.0** to start the frontend service<br /><br />
go to localhost:5173 or your_host:5173

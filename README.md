backend implementation is in "**myproject**" folder


before you run it:<br />


pip install django djangorestframework<br />
pip install django-cors-headers<br />
pip install mysqlclient<br />
pip install mysql-connector-python<br />
pip install djangorestframework-simplejwt<br />
cd into frontend/ to run the npm-started lines:<br />
npm install vue axios vue-router<br />
npm install -D unplugin-vue-components unplugin-auto-import<br />
npm install pinia<br />




**the AWS database is temporarily shutdown**, so please do the following commands <br />
create a mysql database locally, tables are not necessary at this point<br />
configure your local database in **settings.py** first<br />
run the following code in the **myproject/**, the tables will be created according to definitions in **models.py**<br />
python manage.py makemigrations<br />
python manage.py migrate<br />
till this point, tables have been created accordingly.<br />
run the **the_platform.sql** within your local database to inject the prepared data 


how to run it:<br />


cd into myproject and run **python manage.py runserver** to start django <br />
cd into myproject and run **npm run dev** to start vue<br />

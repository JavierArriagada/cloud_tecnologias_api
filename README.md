Instalar una maquina virtual 

- python -m venv venv
- entrar en el ambiente virtual

- modificar credenciales mysql
    Entrar a config/db.py y cambiar credenciales
    engine = create_engine("mysql+pymysql://user:password@localhost:3306/cloud_tecnologias_api")

- en la raiz del proyecto, ejecutar 
    "uvicorn app:app --reload"
    para iniciar api
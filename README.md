# OnyxMessenger
Мессенджер для обмена сообщениями и файлами с красивым и удобным дизайном.
Итоговый командный проект для курса Промышленное программирование в Московской Школе Программистов, 2021

<img src="https://user-images.githubusercontent.com/49102209/234375797-e737a4e5-e358-4380-9ebe-5eb619ca1c82.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/49102209/234375804-fe672dde-fbe2-4396-8313-3d3246c12df0.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/49102209/234375820-e79d9bd4-4ca2-49c8-ac39-6632ee191fbb.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/49102209/234375825-e5764a1b-c5b8-4c31-a63c-50691d4604f0.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/49102209/234375829-6d75540b-a8c5-42c8-8cdd-467619ce8a3c.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/49102209/234375835-29c6a06c-377e-4d27-a11e-cd73e0f035a0.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/49102209/234375837-8a8a97c6-cd65-4c2d-b192-9a27eb44fb4e.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/49102209/234375838-9f0e1c24-2999-4ed4-b068-56948deae19b.png" width="30%"></img> 

## Запуск

### Установка пакетов
```bash
sudo apt install nodejs npm redis-server python3
```

### Бэкенд-сервер:
```bash
cd api
redis-server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Фронтенд-сервера:
```bash
cd web_frontend
npm install
npm run dev
```

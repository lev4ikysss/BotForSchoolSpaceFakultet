echo "Не забудьте установить такие пакеты как: nginx, python3.13"
su root
echo "Создание папки /etc/fakultet"
mkdir -p /etc/fakultet
echo "Создание .venv"
python3 -m venv /etc/fakultet/.venv
echo "Устанавливаю библиотеки"
/etc/fakultet/.venv/bin/pip install -r req.txt
echo "Копирую файлы"
cp -rv * /etc/fakultet
rm -v /etc/fakultet/config/nginx-config
rm -v /etc/fakultet/data/data_example.env
rm -v /etc/fakultet/data/user_data_example.json
rm -v /etc/fakultet/data/tg_id_example.json
rm -v /etc/fakultet/data/vk_id_example.json
rm -v /etc/fakultet/README.md
rm -v /etc/fakultet/.gitignore
rm -v /etc/fakultet/req.txt
cp -v config/nginx-config /etc/nginx/sites-available
cp -v config/nginx-config /etc/nginx/sites-enabled

exit
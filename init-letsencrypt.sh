#!/bin/bash

domains=("tmsns.ru" "www.tmsns.ru")
rsa_key_size=4096
data_path="./lets"
email="azbk2004@gmail.com"

# Вы можете изменить эти параметры согласно вашим требованиям
staging=0 # Измените на 1, чтобы использовать staging-сервер Let's Encrypt

if [ -d "$data_path" ]; then
  read -p "Существующие сертификаты найдены в $data_path. Продолжить замену? (y/N) " decision
  if [ "$decision" != "Y" ] && [ "$decision" != "y" ]; then
    exit
  fi
fi

if [ ! -e "$data_path/conf/options-ssl-nginx.conf" ] || [ ! -e "$data_path/conf/ssl-dhparams.pem" ]; then
  echo "Создаем необходимые файлы конфигурации..."
  mkdir -p "$data_path/conf"
  openssl dhparam -out "$data_path/conf/ssl-dhparams.pem" 2048
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/options-ssl-nginx.conf > "$data_path/conf/options-ssl-nginx.conf"
  echo "Готово"
fi

for domain in "${domains[@]}"; do
  echo "Создаем и регистрируем сертификат для $domain..."
  docker-compose run --rm --entrypoint "\
    certbot certonly --webroot -w /usr/share/nginx/html/ -d $domain \
      --email $email \
      --rsa-key-size $rsa_key_size \
      --agree-tos \
      --no-eff-email \
      --force-renewal" certbot
  echo "Готово"
done

echo "Обновляем конфигурацию Nginx..."
docker-compose restart nginx
echo "Готово"

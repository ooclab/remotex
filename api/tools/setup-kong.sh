## jobx-public-api
api="jobx-public-api"
curl -i -X POST \
  --url http://localhost:8001/apis/ \
  --data 'name=jobx-public-api' \
  --data 'uris=/jobx' \
  --data 'upstream_url=http://127.0.0.1:3001/jobx'
curl -X POST http://localhost:8001/apis/jobx-public-api/plugins \
  --data "name=file-log" \
  --data "config.path=/tmp/kong-jobx-public-api.log"
# cors
curl -X POST http://localhost:8001/apis/${api}/plugins \
    --data "name=cors" \
    --data "config.origins=*" \
    --data "config.methods=GET, POST, DELETE, PUT, PATCH" \
    --data "config.headers=Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, Authorization, X-Auth-Token" \
    --data "config.exposed_headers=X-Auth-Token" \
    --data "config.credentials=true" \
    --data "config.max_age=3600"

## jobx-spider-api
api="jobx-spider-api"
curl -i -X POST \
  --url http://localhost:8001/apis/ \
  --data "name=${api}" \
  --data 'uris=/spider/jobx' \
  --data 'upstream_url=http://127.0.0.1:3001/spider/jobx'
curl -X POST http://localhost:8001/apis/${api}/plugins \
  --data "name=file-log" \
  --data "config.path=/tmp/kong-${api}.log"
# add basic-auth
curl -X POST http://localhost:8001/apis/${api}/plugins \
    --data "name=basic-auth" \
    --data "config.hide_credentials=true"
# create consumer
consumer_username="remotex-spider"
consumer_custom_id="P9hU1d2Gkw5TOEwytdY"
curl -d "username=${consumer_username}&custom_id=${consumer_custom_id}" http://localhost:8001/consumers/
# create credential
credential_username="user1"
credential_password="45aa736f1f66e511a29b0c2b"
curl -X POST http://localhost:8001/consumers/${consumer_username}/basic-auth \
    --data "username=${credential_username}" \
    --data "password=${credential_password}"
token=`echo -en "${credential_username}:${credential_password}" | base64`
echo "Authorization: Basic ${token}"

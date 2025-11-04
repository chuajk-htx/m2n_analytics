## 1. Install clickhouse dbms server (use docker container)

`docker run -d --name clickhouse-server -p 8123:8123 -p 9000:9000 -v "c:\Documents\path\to\dataC:\Users\Admin\Documents\Projects\clickhouse_data:/var/lib/clickhouse" --ulimit nofile=262144:262144 clickhouse/clickhouse-server`

- `-p 8123:8123` --> HTTP interface (for Python client)
- `-p 9000:9000` --> Native protocol (faster queries)
- `--ulimit nofile=262144:262144` --> CRITICAL: Allow 262,144 open files
- `-v "c:\Documents\path\to\data:/var/lib/clickhouse"` --> volume mount <local_data_dir>:<container_dir_path>

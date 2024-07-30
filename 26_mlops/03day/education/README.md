# Docker 관련세팅

```sh
poetry new mysql
cd mysql
rm -r tests
mv mysql mysql_connection
# mac에선 sed -i 옵션뒤에 항상 파라미터가 필요함 ''
sed -i '' 's/mysql/mysql_connection/g' pyproject.toml
# 나머지 pyproject.toml 작성 (생략)
poetry add pymysql pandas openpyxl
poetry install
poetry shell
```

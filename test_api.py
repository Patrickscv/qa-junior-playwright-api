import random 
import string
from faker import Faker
import logging

faker = Faker()
# Classe responsável por testar os verbos GET e PUT  de um usuário
class TestUser:
    def test_get_user(self, test_url_token, create_user):
        id_user = create_user["id"]
        url = f"/public/v2/users/{id_user}"
        response = test_url_token.get(url)
        response_json = response.json()
        
        assert response.status == 200
        assert response_json["id"] == id_user
        assert response_json["name"] == create_user["name"]
        assert response_json["email"] == create_user["email"]
        assert response_json["gender"] == create_user["gender"]
        assert response_json["status"] == create_user["status"]

        logging.info(f"Informações do usuário acessadas com Sucesso! - status code: {response.status}")

    def test_put_user(self, test_url_token, create_user):
        id_user = create_user["id"]
        infos = {
            "name": faker.name(),
            "email": faker.email()
        }
        url = f"/public/v2/users/{id_user}"
        response = test_url_token.put(url, data=infos)
        response_json = response.json()

        assert response.status == 200
        assert "id" in response_json
        assert "gender" in response_json
        assert "status" in response_json
        assert response_json["name"] == infos["name"]
        assert response_json["email"] == infos["email"]

        logging.info(f"Informações do usuário alteradas com Sucesso! - status code: {response.status}")

# Classe responsável por testar os verbos GET e PUT de um post
class TestPost:
    def test_get_post(self, test_url_token, create_post):
        id_post = create_post["id"]
        url = f"/public/v2/posts/{id_post}"
        response = test_url_token.get(url)
        response_json = response.json()

        assert response.status == 200
        assert response_json["id"] == id_post
        assert response_json["user_id"] == create_post["user_id"]
        assert response_json["title"] == create_post["title"]
        assert response_json["body"] == create_post["body"]
        
        logging.info(f"Informações do Post acessadas com Sucesso! - status code: {response.status}")

    def test_put_post(self, test_url_token, create_post):
        id_post = create_post["id"]
        infos = {
            "title": faker.text(),
            "body": faker.text()
        }
        url = f"/public/v2/posts/{id_post}"
        response = test_url_token.put(url, data=infos)
        response_json = response.json()

        assert response.status == 200
        assert "id" in response_json
        assert "user_id" in response_json
        assert infos["title"] == response_json["title"]
        assert infos["body"] == response_json["body"]

        logging.info(f"Informações do post alteradas com Sucesso! - status code: {response.status}")

# Classe responsável por testar os verbos GET e PUT de um comentário
class TestComment:
    def test_get_comment(self, test_url_token, create_comment):
        id_comment = create_comment["id"]
        url = f"/public/v2/comments/{id_comment}"
        response = test_url_token.get(url)
        response_json = response.json()

        assert response.status == 200
        assert response_json["id"] == id_comment
        assert response_json["post_id"] == create_comment["post_id"]
        assert response_json["name"] == create_comment["name"]
        assert response_json["email"] == create_comment["email"]
        assert response_json["body"] == create_comment["body"]
        
        logging.info(f"Informações do comentário acessadas com Sucesso! - status code: {response.status}")

    def test_put_comment(self, test_url_token, create_comment):
        id_comment = create_comment["id"]
        infos = {
            "name": faker.name(),
            "email": faker.email(),
            "body": faker.text()
        }
        url = f"/public/v2/comments/{id_comment}"
        response = test_url_token.put(url, data=infos)
        response_json = response.json()

        assert response.status == 200
        assert "post_id" in response_json
        assert "id" in response_json
        assert response_json["name"] == infos["name"]
        assert response_json["email"] == infos["email"]
        assert response_json["body"] == infos["body"]

        logging.info(f"Informações do comentário alteradas com Sucesso! - status code: {response.status}")

        
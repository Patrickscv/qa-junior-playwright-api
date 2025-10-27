from dotenv import load_dotenv
import os
import pytest
import playwright
from faker import Faker
import logging

faker = Faker()

load_dotenv()

@pytest.fixture(scope="session")
def test_base_url():
    return os.getenv("BASE_URL")

@pytest.fixture(scope="session")
def test_access_token():
    return os.getenv("ACCESS_TOKEN")

#fixture principal, que cria a URL contendo o base_url e o access_token
@pytest.fixture(scope="session")
def test_url_token(playwright, test_base_url, test_access_token):
    headers = {
        "Authorization": f"Bearer {test_access_token}",
        "Content-Type": "application/json"
    }

    url_full = playwright.request.new_context(
        base_url = test_base_url,
        extra_http_headers=headers
    )

    yield url_full

    url_full.dispose()

#Fixture responsável por criar um usuário
@pytest.fixture(scope="session")
def create_user(test_url_token):
        infos = {
            "name": faker.name(),
            "email": faker.email(),
            "gender": "male",
            "status": "active"
        }

        url = "/public/v2/users"
        response = test_url_token.post(url, data=infos)
        response_json = response.json()

        assert response.status == 201
        assert "id" in response_json
        assert infos["name"] == response_json["name"]
        assert infos["email"] == response_json["email"]
        assert infos["gender"] == response_json["gender"]
        assert infos["status"] == response_json["status"]

        logging.info(f"Usuário Criado com Sucesso! - status code: {response.status}")

        yield response_json
        
        #Realiza o Delete do usuário
        id_user = response_json["id"]
        url_delete = f"/public/v2/users/{id_user}"
        delete_user = test_url_token.delete(url_delete)

        assert delete_user.status == 204

        logging.info(f"Usuário Deletado com Sucesso! - status code: {delete_user.status}")
        
        #Valida se foi deletado corretamente
        url_verify = f"/public/v2/users/{id_user}"
        verify_delete = test_url_token.get(url_verify)
        
        assert verify_delete.status == 404

#Fixture responsável por criar um post, deletar e validar se foi excluido.
@pytest.fixture(scope="session")
def create_post(test_url_token, create_user): 
        id_user = create_user["id"]
        infos = {
            "user_id": id_user,
            "title": faker.text(),
            "body": faker.text()
        }
        url = "/public/v2/posts"
        response = test_url_token.post(url, data=infos)
        response_json = response.json()

        assert response.status == 201
        assert "id" in response_json
        assert response_json["user_id"] == id_user
        assert response_json["title"] == infos["title"]
        assert response_json["body"] == infos["body"]

        logging.info(f"Post Criado com Sucesso! - status code: {response.status}")

        yield response_json

        id_post = response_json["id"]
        url_delete = f"/public/v2/posts/{id_post}"
        delete_post = test_url_token.delete(url_delete)

        #Realiza o Delete do Post
        assert delete_post.status == 204

        logging.info(f"Post Deletado com Sucesso! - status code: {delete_post.status}")

        #Valida se foi deletado corretamente
        url_verify = f"/public/v2/posts/{id_post}"
        verify_delete = test_url_token.get(url_verify)

        assert verify_delete.status == 404

#Fixture responsável por criar um comentário
@pytest.fixture(scope="session")
def create_comment(test_url_token, create_post):
        id_post = create_post["id"]
        infos = {
            "post_id": id_post,
            "name": faker.name(),
            "email": faker.email(),
            "body": faker.text()
        }

        url = f"/public/v2/comments"
        response = test_url_token.post(url, data=infos)
        response_json = response.json()

        assert response.status == 201
        assert "id" in response_json
        assert infos["post_id"] == response_json["post_id"]
        assert infos["name"] == response_json["name"]
        assert infos["email"] == response_json["email"]
        assert infos["body"] == response_json["body"]

        logging.info(f"Comentário Criado com Sucesso! - status code: {response.status}")

        yield response_json

        #Realiza o Delete do comentário
        id_comment = response_json["id"]
        url_delete = f"/public/v2/comments/{id_comment}"
        delete_comment = test_url_token.delete(url_delete)

        assert delete_comment.status == 204
        
        logging.info(f"Comentário Deletado com Sucesso! - status code: {delete_comment.status}")

        #Valida se foi deletado corretamente
        url_verify = f"/public/v2/comments/{id_comment}"
        verify_delete = test_url_token.get(url_verify)

        assert verify_delete.status == 404

        
        

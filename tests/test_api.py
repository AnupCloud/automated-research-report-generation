"""
Tests for the FastAPI application endpoints.
"""

import pytest
from httpx import ASGITransport, AsyncClient

from research_and_analyst.api.main import app


@pytest.fixture
def transport():
    return ASGITransport(app=app)


@pytest.fixture
async def client(transport):
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


class TestHealthEndpoint:
    @pytest.mark.asyncio
    async def test_health_check_returns_200(self, client):
        response = await client.get("/health")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_health_check_response_body(self, client):
        response = await client.get("/health")
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "research-report-generation"
        assert "timestamp" in data


class TestLoginPage:
    @pytest.mark.asyncio
    async def test_login_page_returns_200(self, client):
        response = await client.get("/")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_login_page_contains_form(self, client):
        response = await client.get("/")
        assert "Login" in response.text or "login" in response.text


class TestSignupPage:
    @pytest.mark.asyncio
    async def test_signup_page_returns_200(self, client):
        response = await client.get("/signup")
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_signup_page_contains_form(self, client):
        response = await client.get("/signup")
        assert "Signup" in response.text or "signup" in response.text or "Sign" in response.text


class TestDashboardAuth:
    @pytest.mark.asyncio
    async def test_dashboard_redirects_without_session(self, client):
        """Accessing dashboard without a session cookie should redirect to login."""
        response = await client.get("/dashboard", follow_redirects=False)
        assert response.status_code in (302, 307)

    @pytest.mark.asyncio
    async def test_login_with_invalid_credentials(self, client):
        """Login with wrong credentials should return login page with error."""
        response = await client.post(
            "/login",
            data={"username": "nonexistent", "password": "wrongpass"},
        )
        assert response.status_code == 200
        assert "Invalid" in response.text or "invalid" in response.text or "error" in response.text.lower()

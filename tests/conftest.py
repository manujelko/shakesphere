def pytest_configure(config):
    config.addinivalue_line("markers", "integration: mark as integration tests")

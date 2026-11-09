def create_document_payload(document_id="DOC-TEST-001"):
    return {
        "document_id": document_id,
        "filename": "sample-invoice.pdf",
        "content_type": "application/pdf",
        "file_size": 1024,
    }


def test_register_document_success(client):
    response = client.post(
        "/api/v1/documents/",
        json=create_document_payload(),
    )

    assert response.status_code == 201

    data = response.json()

    assert data["document_id"] == "DOC-TEST-001"
    assert data["filename"] == "sample-invoice.pdf"
    assert data["content_type"] == "application/pdf"
    assert data["file_size"] == 1024
    assert data["status"] == "uploaded"
    assert "id" in data
    assert "created_at" in data


def test_duplicate_document_id_returns_conflict(client):
    payload = create_document_payload()

    first_response = client.post(
        "/api/v1/documents/",
        json=payload,
    )

    second_response = client.post(
        "/api/v1/documents/",
        json=payload,
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 409


def test_invalid_document_id_returns_validation_error(client):
    payload = create_document_payload(document_id="INVALID-001")

    response = client.post(
        "/api/v1/documents/",
        json=payload,
    )

    assert response.status_code == 422


def test_negative_file_size_returns_validation_error(client):
    payload = create_document_payload()
    payload["file_size"] = -100

    response = client.post(
        "/api/v1/documents/",
        json=payload,
    )

    assert response.status_code == 422


def test_get_document_by_id(client):
    payload = create_document_payload()

    create_response = client.post(
        "/api/v1/documents/",
        json=payload,
    )

    assert create_response.status_code == 201

    response = client.get("/api/v1/documents/DOC-TEST-001")

    assert response.status_code == 200
    assert response.json()["document_id"] == "DOC-TEST-001"


def test_get_missing_document_returns_not_found(client):
    response = client.get("/api/v1/documents/DOC-DOES-NOT-EXIST")

    assert response.status_code == 404


def test_list_documents(client):
    first_payload = create_document_payload("DOC-TEST-001")
    second_payload = create_document_payload("DOC-TEST-002")

    first_response = client.post(
        "/api/v1/documents/",
        json=first_payload,
    )

    second_response = client.post(
        "/api/v1/documents/",
        json=second_payload,
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 201

    response = client.get("/api/v1/documents/")

    assert response.status_code == 200

    documents = response.json()

    assert len(documents) == 2

    document_ids = {
        document["document_id"] for document in documents
    }

    assert document_ids == {"DOC-TEST-001", "DOC-TEST-002"}


def test_whitespace_only_filename_returns_validation_error(client):
    payload = create_document_payload()
    payload["filename"] = "   "

    response = client.post(
        "/api/v1/documents/",
        json=payload,
    )

    assert response.status_code == 422


def test_document_id_with_invalid_characters_returns_validation_error(client):
    payload = create_document_payload("DOC-INVALID@123")

    response = client.post(
        "/api/v1/documents/",
        json=payload,
    )

    assert response.status_code == 422


def test_file_size_boolean_returns_validation_error(client):
    payload = create_document_payload()
    payload["file_size"] = True

    response = client.post(
        "/api/v1/documents/",
        json=payload,
    )

    assert response.status_code == 422


def test_filename_is_trimmed_before_storage(client):
    payload = create_document_payload()
    payload["filename"] = "   invoice.pdf   "

    response = client.post(
        "/api/v1/documents/",
        json=payload,
    )

    assert response.status_code == 201
    assert response.json()["filename"] == "invoice.pdf"

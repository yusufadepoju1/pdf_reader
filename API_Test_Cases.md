# API TEST CASES

Endpoint

POST /upload

Positive Tests

- Upload valid PDF
- Upload multi-page PDF
- Upload table PDF
- Upload text PDF

Negative Tests

- Missing file
- Empty request
- TXT file
- DOCX file
- PNG file
- ZIP file
- Corrupted PDF
- Password protected PDF

Expected Response

200 OK for successful upload

400 Bad Request for invalid request

500 Internal Server Error should never be exposed to users.
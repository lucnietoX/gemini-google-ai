model = genai.GenerativeModel('gemini-1.5-flash')

cookie_picture = {
    'mime_type': 'image/png',
    'data': pathlib.Path('cookie.png').read_bytes()
}
prompt = "Do these look store-bought or homemade?"

response = model.generate_content(
    model="gemini-1.5-flash",
    content=[prompt, cookie_picture]
)
print(response.text)

#reference: https://ai.google.dev/gemini-api/docs/api-overview

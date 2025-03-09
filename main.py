<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Facebook Token</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .container { background: white; width: 400px; padding: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); border-radius: 10px; text-align: center; }
        textarea, input { width: 100%; padding: 10px; margin: 10px 0; font-size: 16px; border: 1px solid #ddd; border-radius: 5px; }
        button { padding: 10px 20px; font-size: 16px; background-color: #28a745; color: white; border: none; cursor: pointer; border-radius: 5px; }
        button:hover { background-color: #218838; }
        .output { margin-top: 20px; font-size: 16px; color: #333; }
        .copy-button { margin-top: 10px; padding: 5px 10px; font-size: 14px; background-color: #007bff; color: white; border: none; cursor: pointer; border-radius: 5px; }
        .copy-button:hover { background-color: #0056b3; }
    </style>
    <script>
        function copyToClipboard() {
            let tokenField = document.getElementById("token");
            navigator.clipboard.writeText(tokenField.innerText).then(() => {
                alert("Token copied to clipboard!");
            });
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>Get Facebook Token</h1>
        <p>Enter your Facebook cookie below:</p>
        <form method="post">
            <textarea name="cookie" rows="5" placeholder="Enter your Facebook cookie here..."></textarea><br>
            <button type="submit">Get Token</button>
        </form>

        {% if token %}
        <div class="output">
            <p>Extracted Token:</p>
            <textarea id="token" rows="3" readonly>{{ token }}</textarea>
            <button class="copy-button" onclick="copyToClipboard()">Copy</button>
        </div>
        {% endif %}
    </div>
</body>
</html>

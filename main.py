<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KRISH CHEAKPOINT</title>
    <style>
        body {
            font-family: sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f0f0f0; /* Light gray background */
        }

        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            text-align: center; /* Center the content */
        }

        img {
            max-width: 200px; /* Adjust image size as needed */
            margin-bottom: 20px;
        }

        input[type="password"] {
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            width: 200px; /* Set a specific width */
            box-sizing: border-box; /* Include padding and border in the element's total width and height */
        }

        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        #message {
            margin-top: 10px;
            color: red; /* Set default color to red for errors */
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://i.ibb.co/X0bbjMz/20250214-124029.jpg" alt="Your Image">  <input type="password" id="password" placeholder="Enter password">
        <button onclick="checkPassword()">Submit</button>
        <div id="message"></div> </div>

    <script>
        function checkPassword() {
            const enteredPassword = document.getElementById("password").value;
            const messageDiv = document.getElementById("message");
            const correctPassword = "KRISH07"; // Replace with your actual password

            if (enteredPassword === correctPassword) {
                messageDiv.textContent = ""; // Clear any previous error message
                // Redirect or open link in a new tab
                window.location.href = "https://apk-krish.onrender.com"; // Replace with your desired link
                // Or to open in new tab:
                // window.open("your_link_here", "_blank");
            } else {
                messageDiv.textContent = "Enter Authorised Password";
            }
        }
    </script>

</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

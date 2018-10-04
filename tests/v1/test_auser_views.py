
"""
    Mock signup data to test the working of user sign up
"""

mock_reg = [{"email": "", "username": "delight", "password": "delight", "confirm_password": "delight"},
            {"email": "yagamidelightgmail.com", "username": "delight",
             "password": "delight", "confirm_password": "delight"},
            {"email": "yagamidelight@gmail", "username": "delight",
             "password": "delight", "confirm_password": "delight"},
            {"email": 123454, "username": "delight",
             "password": "delight", "confirm_password": "delight"},

            {"email": "yagamidelight@gmail.com", "username": "delight",
             "password": "string@12", "confirm_password": "string@12"},

            {"email": "yagamidelight@gmail.com", "username": "delight",
             "password": 123, "confirm_password": 123},
            {"email": "yagamidelight@gmail.com", "username": "delight",
             "password": "delight@11", "confirm_password": "delight@1"},
            {"email": "yagamidelight@gmail.com", "username": "delight",
             "password": "deli", "confirm_password": "deli"},

            {"email": "yagamidelight@gmail.com", "username": 12334,
             "password": "delight", "confirm_password": "delight"},
            {"email": "yagamidelight@gmail.com", "username": "",
             "password": "delight", "confirm_password": "delight"},
            {"email": "yagamidelight@gmail.com", "username": "      ",
            "password": "delight", "confirm_password": "delight"},
            {"email": "testfast@food.com", "username": "fast-food-fast", "password": "Admintester", "confirm_password": "Admintester"},
            {}]

"""
    Mock Signin data to test the working of user signin
"""

mock_log = [{"email": 123, "password": "delight"},
            {"email": "", "password": "delight"},
            {"email": "yagamidelight.com", "password": "delight"},
            {"email": "yagamidelight@gmail", "password": "delight"},

            {"email": "yagamidelight@gmail.com", "password": 123},
            {"email": "yagamidelight@gmail.com", "password": "deli"},

            {"email": "yagamidelight@gmail.com", "password": "string@12"},
            {"email": "testfast@food.com", "password": "Admintester"},
            {},{"email": "yagamidelight@gmail.com", "password": "string@12345"},
            {"email": "user@gmx.com", "password": "stranger12345"}]

import instaloader
i = instaloader.Instaloader()
username = input('Enter username :-')
i.download_profile(username, profile_pic_only=True)
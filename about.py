def about():
  class AboutMeWindow(tk.Tk):
      def __init__(self, photo_path, name, email):
          super().__init__()
          self.title("About Me")
          self.geometry("400x480")

          # Open image and create circle mask
          image = Image.open(photo_path)
          image = image.resize((200, 200))  # Resize image to fit window
          mask = Image.new("L", (200, 200), 0)
          draw = ImageDraw.Draw(mask)
          draw.ellipse((0, 0, 200, 200), fill=255)

          # Apply mask to image
          image.putalpha(mask)
          photo = ImageTk.PhotoImage(image)

          # Create label for photo
          photo_label = tk.Label(self, image=photo)
          photo_label.image = photo
          photo_label.pack(pady=10)

          # Create label for name
          name_label = tk.Label(self, text=name, font=("Arial", 16))
          name_label.pack(pady=5)

          # Create label for email
          email_label = tk.Label(self, text=email, font=("Arial", 12))
          email_label.pack(pady=5)

          # Create button to send email
          def send_email():
              webbrowser.open(f"mailto:{email}")
          email_button = tk.Button(self, text="Send Email", command=send_email)
          email_button.pack(pady=5)

          # Create button to open LinkedIn profile
          def open_linkedin():
              webbrowser.open(f"https://www.linkedin.com/in/ali-ahammad-li0812/")
          linkedin_button = tk.Button(self, text="View LinkedIn Profile", command=open_linkedin)
          linkedin_button.pack(pady=5)

          # Create button to open GitHub profile
          def open_github():
              webbrowser.open(f"https://github.com/li812")
          github_button = tk.Button(self, text="View GitHub Profile", command=open_github)
          github_button.pack(pady=5)

          # Create button to open Instagram profile
          def open_instagram():
              webbrowser.open(f"https://www.instagram.com/the_raptor_rider_/")
          instagram_button = tk.Button(self, text="View Instagram Profile", command=open_instagram)
          instagram_button.pack(pady=5)



  if __name__ == '__main__':
      window = AboutMeWindow("src/pic.png", "Ali Ahammad", "aliahammad0812@outlook.com")
      close_button = tk.Button(window, text="Close", command=window.destroy)
      close_button.pack(pady=5)
      window.mainloop()
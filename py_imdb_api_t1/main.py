from tkinter import *
import urllib.request
from tkinter import Tk, Label
from PIL import Image, ImageTk
import requests
import io

window = Tk()
window.geometry('500x750')
window.title("Welcome to IMDB API")
window.grid_columnconfigure(0, weight=1)
window.config(padx=30, pady=30)


def text_search():
    if text_input.get():
        user_input = text_input.get()
        endpoint = "https://www.omdbapi.com/"
        api_key = "76ac3b92"
        my_params = {
            "t": user_input,
            "apikey": api_key
        }
        response = requests.get(endpoint, params=my_params)
        # text_response = response.text
        print(response.status_code)
        result_dict = response.json()

        # Received my important data from response
        result_dict_released = result_dict["Released"]
        result_dict_poster = result_dict["Poster"]
        result_dict_genre = result_dict["Genre"]
        result_dict_actors = result_dict["Actors"]
        # result_dict_plot = result_dict["Plot"]
        result_dict_country = result_dict["Country"]
        result_dict_awards = result_dict["Awards"]
        result_dict_rate = result_dict["imdbRating"]
        # Display the result of data with creating label
        Label(window, text=f"Released : {result_dict_released}").grid(row=3)
        Label(window, text=f"Country : {result_dict_country}").grid(row=4)
        Label(window, text=f"Genre : {result_dict_genre}").grid(row=5)
        Label(window, text=f"Actors : {result_dict_actors}").grid(row=6)
        # Label(window, text=result_dict_plot).grid(row=7)
        Label(window, text=f"Awards : {result_dict_awards}").grid(row=8)
        Label(window, text=f"Rating : {result_dict_rate}").grid(row=9)

        # Open URL and load image
        with urllib.request.urlopen(result_dict_poster) as u:
            raw_data = u.read()

        # Open the image and convert it to ImageTk format
        im = Image.open(io.BytesIO(raw_data))
        img = ImageTk.PhotoImage(im)

        # Create a label and add the image to it
        Label(window, image=img).grid(row=10).pack()

    else:
        Label(window, text="Text input cannot be empty").grid(row=3)


Label(window, text="insert a title of movie correctly:", font=("Helvetica", 14)).grid(column=0, row=0, sticky="N",
                                                                                      padx=20,
                                                                                      pady=10)
text_input = Entry(window)
text_input.grid(row=1, column=0, sticky="WE", padx=10)

canvas = Canvas(window, width=300, height=300)

search_button = Button(window, text="Search", bg="yellow", command=text_search)
search_button.grid(row=2, column=0, sticky="WE", padx=10, pady=10)

if __name__ == "__main__":
    window.mainloop()

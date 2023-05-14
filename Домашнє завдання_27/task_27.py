import tkinter as tk
import json
import os


def submit():
  name = name_entry.get()
  address1 = address1_entry.get()
  address2 = address2_entry.get()
  city = city_entry.get()
  region = region_entry.get()
  zip_code = zip_entry.get()
  name_label.config(fg='black')
  address1_label.config(fg='black')
  city_label.config(fg='black')
  region_label.config(fg='black')
  zip_label.config(fg='black')
  if not all([name, address1, city, region, zip_code]):
    status_label.config(text="Не всі поля заповнено!", fg="red")
    if not name:
      name_label.config(fg='red')
    if not address1:
      address1_label.config(fg='red')
    if not city:
      city_label.config(fg='red')
    if not region:
      region_label.config(fg='red')
    if not zip_code:
      zip_label.config(fg='red')
    window.title("Не всі поля заповнено!")
  else:
    result = []
    if os.path.exists('data.json'):
      with open("data.json", "r") as f:
        result = json.load(f)

    data = {
      "name": name,
      "address1": address1,
      "address2": address2,
      "city": city,
      "region": region,
      "zip_code": zip_code
    }

    result.append(data)

    with open("data.json", "w") as f:
      json.dump(result, f, indent=4)

    status_label.config(text=f"{name}, ваші дані успішно відправлено",
                        fg="black")
    window.title(f"{name}, ваші дані успішно відправлено")


def clear():
  name_entry.delete(0, "end")
  address1_entry.delete(0, "end")
  address2_entry.delete(0, "end")
  city_entry.delete(0, "end")
  region_entry.delete(0, "end")
  zip_entry.delete(0, "end")
  status_label.config(text="Уведіть дані", fg="black")


window = tk.Tk()
window.geometry('400x350')
window.title("Уведіть дані")
window.grid_columnconfigure(0, weight=1)

name_label = tk.Label(window, text="Имʼя:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

address1_label = tk.Label(window, text="Адреса 1:")
address1_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

address1_entry = tk.Entry(window)
address1_entry.grid(row=1, column=1, padx=10, pady=10)

address2_label = tk.Label(window, text="Адреса 2:")
address2_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

address2_entry = tk.Entry(window)
address2_entry.grid(row=2, column=1, padx=10, pady=10)

city_label = tk.Label(window, text="Місто:")
city_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

city_entry = tk.Entry(window)
city_entry.grid(row=3, column=1, padx=10, pady=10)

region_label = tk.Label(window, text="Область:")
region_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

region_entry = tk.Entry(window)
region_entry.grid(row=4, column=1, padx=10, pady=10)

zip_label = tk.Label(window, text="Поштовий індекс:")
zip_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")

zip_entry = tk.Entry(window)
zip_entry.grid(row=5, column=1, padx=10, pady=10)

submit_button = tk.Button(window, text="Відправити", command=submit)
submit_button.grid(row=6, column=0, padx=10, pady=10)

status_label = tk.Label(window)
status_label.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

clear_button = tk.Button(window, text="Очистити", command=clear)
clear_button.grid(row=6, column=1, padx=10, pady=10)

window.mainloop()

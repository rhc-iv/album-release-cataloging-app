import json
import uuid
from tkinter import *
from tkinter import ttk

global my_data_list
global currentRowIndex

my_data_list = []

root = Tk()
root.title('Album Release Cataloging App')
root.geometry('1500x940')
root.configure(bg='#282C34')

style = ttk.Style()
style.configure(
    "mystyle.Treeview",
    highlightthickness=0,
    bd=0,
    font=(
        'SF Pro Display',
        12,
    ),
    bg='#3E4451',
    fg='#D19A66',
)

input_frame = LabelFrame(
    root,
    borderwidth=5,
    text='Release Info',
    bg='#565C64',
    fg='#D19A66',
    font=(
        'SF Pro Display',
        20,
        'bold',
    ),
    relief='sunken',
    width=1495,
)
input_frame.grid(row=0, column=0, rowspan=5, columnspan=6)

l1 = Label(
    input_frame,
    anchor='e',
    bg='#3E4451',
    fg='#D19A66',
    width=45,
    height=1,
    relief='ridge',
    text="ID",
    font=(
        'SF Pro Display',
        20,
        'bold',
    ),
    padx=20,
    pady=5,
).grid(row=1, column=0)

l2 = Label(
    input_frame,
    anchor='e',
    bg='#3E4451',
    fg='#D19A66',
    width=45,
    height=1,
    relief='ridge',
    text='Artist',
    font=(
        'SF Pro Display',
        20,
        'bold',
    ),
    padx=20,
    pady=5,
).grid(row=2, column=0)

l3 = Label(
    input_frame,
    anchor='e',
    bg='#3E4451',
    fg='#D19A66',
    width=45,
    height=1,
    relief='ridge',
    text='Title',
    font=(
        'SF Pro Display',
        20,
        'bold',
    ),
    padx=20,
    pady=5,
).grid(row=3, column=0)

l4 = Label(
    input_frame,
    anchor='e',
    bg='#3E4451',
    fg='#D19A66',
    width=45,
    height=1,
    relief='ridge',
    text='Album',
    font=(
        'SF Pro Display',
        20,
        'bold',
    ),
    padx=20,
    pady=5,
).grid(row=4, column=0)

l5 = Label(
    input_frame,
    anchor='e',
    bg='#3E4451',
    fg='#D19A66',
    width=45,
    height=1,
    relief='ridge',
    text='Year',
    font=(
        'SF Pro Display',
        20,
        'bold',
    ),
    padx=20,
    pady=5,
).grid(row=5, column=0)

l6 = Label(
    input_frame,
    anchor='e',
    bg='#3E4451',
    fg='#D19A66',
    width=45,
    height=1,
    relief='ridge',
    text='Genre',
    font=(
        'SF Pro Display',
        20,
        'bold',
    ),
    padx=20,
    pady=5,
).grid(row=6, column=0)

l7 = Label(
    input_frame,
    anchor='e',
    bg='#3E4451',
    fg='#D19A66',
    width=45,
    height=1,
    relief='ridge',
    text='BPM',
    font=(
        'SF Pro Display',
        20,
        'bold',
    ),
    padx=20,
    pady=5,
).grid(row=7, column=0)

l8 = Label(
    input_frame,
    anchor='e',
    bg='#3E4451',
    fg='#D19A66',
    width=45,
    height=1,
    relief='ridge',
    text='Key',
    font=(
        'SF Pro Display',
        20,
        'bold',
    ),
    padx=20,
    pady=5,
).grid(row=8, column=0)

l9 = Label(
    input_frame,
    anchor='e',
    bg='#3E4451',
    fg='#D19A66',
    width=45,
    height=1,
    relief='ridge',
    text='Record Label',
    font=(
        'SF Pro Display',
        20,
        'bold',
    ),
    padx=20,
    pady=5,
).grid(row=9, column=0)

l10 = Label(
    input_frame,
    anchor='e',
    bg='#3E4451',
    fg='#D19A66',
    width=45,
    height=1,
    relief='ridge',
    text='Catalog No.',
    font=(
        'SF Pro Display',
        20,
        'bold',
    ),
    padx=20,
    pady=5,
).grid(row=10, column=0)

id_value = StringVar()
id_value.set(uuid.uuid4())

arca_id = Label(
    input_frame,
    anchor='w',
    width=64,
    height=1,
    relief='groove',
    textvariable=id_value,
    bg='#C8CCD4',
    fg='#282C34',
    font=(
        'SF Pro Display',
        18,
        'bold',
    ),
    padx=20,
    pady=5,
)
arca_id.grid(row=1, column=1)

arca_artist = Entry(
    input_frame,
    width=73,
    bg='#C8CCD4',
    fg='#282C34',
    font=(
        'SF Pro Display',
        18,
    ),
    relief='groove',
)
arca_artist.grid(row=2, column=1, columnspan=2)

arca_title = Entry(
    input_frame,
    width=73,
    bg='#C8CCD4',
    fg='#282C34',
    font=(
        'SF Pro Display',
        18,
    ),
    relief='groove',
)
arca_title.grid(row=3, column=1, columnspan=2)

arca_album = Entry(
    input_frame,
    width=73,
    bg='#C8CCD4',
    fg='#282C34',
    font=(
        'SF Pro Display',
        18,
    ),
    relief='groove',
)
arca_album.grid(row=4, column=1, columnspan=2)

arca_year = Entry(
    input_frame,
    width=73,
    bg='#C8CCD4',
    fg='#282C34',
    font=(
        'SF Pro Display',
        18,
    ),
    relief='groove',
)
arca_year.grid(row=5, column=1, columnspan=2)

arca_genre = Entry(
    input_frame,
    width=73,
    bg='#C8CCD4',
    fg='#282C34',
    font=(
        'SF Pro Display',
        18,
    ),
    relief='groove',
)
arca_genre.grid(row=6, column=1, columnspan=2)

arca_bpm = Entry(
    input_frame,
    width=73,
    bg='#C8CCD4',
    fg='#282C34',
    font=(
        'SF Pro Display',
        18,
    ),
    relief='groove',
)
arca_bpm.grid(row=7, column=1, columnspan=2)

arca_song_key = Entry(
    input_frame,
    width=73,
    bg='#C8CCD4',
    fg='#282C34',
    font=(
        'SF Pro Display',
        18,
    ),
    relief='groove',
)
arca_song_key.grid(row=8, column=1, columnspan=2)

arca_rec_label = Entry(
    input_frame,
    width=73,
    bg='#C8CCD4',
    fg='#282C34',
    font=(
        'SF Pro Display',
        18,
    ),
    relief='groove',
)
arca_rec_label.grid(row=9, column=1, columnspan=2)

arca_cat_no = Entry(
    input_frame,
    width=73,
    bg='#C8CCD4',
    fg='#282C34',
    font=(
        'SF Pro Display',
        18,
    ),
    relief='groove',
)
arca_cat_no.grid(row=10, column=1, columnspan=2)

trv = ttk.Treeview(
    root,
    columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    show='headings',
    height='24',
    style='mystyle.Treeview',
)
trv.grid(row=11, column=0, rowspan=16, columnspan=8)

trv.heading(1, text='ID', anchor='center')
trv.heading(2, text='Artist', anchor='center')
trv.heading(3, text='Title', anchor='center')
trv.heading(4, text='Album', anchor='center')
trv.heading(5, text='Year', anchor='center')
trv.heading(6, text='Genre', anchor='center')
trv.heading(7, text='BPM', anchor='center')
trv.heading(8, text='Key', anchor='center')
trv.heading(9, text='Record Label', anchor='center')
trv.heading(10, text='Catalog No.', anchor='center')

trv.column('#1', anchor='w', width=200, stretch=True)
trv.column('#2', anchor='w', width=147, stretch=True)
trv.column('#3', anchor='w', width=147, stretch=True)
trv.column('#4', anchor='w', width=147, stretch=True)
trv.column('#5', anchor='w', width=147, stretch=True)
trv.column('#6', anchor='w', width=147, stretch=True)
trv.column('#7', anchor='w', width=147, stretch=True)
trv.column('#8', anchor='w', width=147, stretch=True)
trv.column('#9', anchor='w', width=147, stretch=True)
trv.column('#10', anchor='w', width=147, stretch=True)


def load_json_from_file():
    global my_data_list
    with open('music.json', 'r') as file_handler:
        my_data_list = json.load(file_handler)
    file_handler.close
    print('File has been read and closed!')


def save_json_to_file():
    global my_data_list
    with open('music.json', 'w') as file_handler:
        json.dump(my_data_list, file_handler, indent=4)
    file_handler.close
    print('File has been written to and closed!')


def remove_all_data_from_trv():
    for item in trv.get_children():
        trv.delete(item)


def load_trv_with_json():
    global my_data_list

    remove_all_data_from_trv()

    rowIndex = 1

    for key in my_data_list:
        guid_value = key['id']
        artist = key['artist']
        title = key['title']
        album = key['album']
        year = key['year']
        genre = key['genre']
        bpm = key['bpm']
        song_key = key['song_key']
        rec_label = key['rec_label']
        catalog_no = key['catalog_no']

        trv.insert(
            '',
            index='end',
            iid=rowIndex,
            text='',
            values=(
                guid_value,
                artist,
                title,
                album,
                year,
                genre,
                bpm,
                song_key,
                rec_label,
                catalog_no
            )
        )
        rowIndex = rowIndex + 1


def clear_all_fields():
    arca_artist.delete(0, END)
    arca_title.delete(0, END)
    arca_album.delete(0, END)
    arca_year.delete(0, END)
    arca_genre.delete(0, END)
    arca_bpm.delete(0, END)
    arca_song_key.delete(0, END)
    arca_rec_label.delete(0, END)
    arca_cat_no.delete(0, END)
    arca_id.configure(text='')
    arca_artist.focus_set()
    id_value.set(uuid.uuid4())
    change_background_color('#E0E0E0')


def find_row_in_my_data_list(guid_value):
    global my_data_list
    row = 0
    found = False

    for rec in my_data_list:
        if rec['id'] == guid_value:
            found = True
            break
        row = row + 1

    if (found == True):
        return (row)

    return (-1)


def change_background_color(new_color):
    arca_artist.config(bg=new_color)
    arca_title.config(bg=new_color)
    arca_album.config(bg=new_color)
    arca_year.config(bg=new_color)
    arca_genre.config(bg=new_color)
    arca_bpm.config(bg=new_color)
    arca_song_key.config(bg=new_color)
    arca_rec_label.config(bg=new_color)
    arca_cat_no.config(bg=new_color)


def change_enabled_state(state):
    if state == 'Edit':
        btnUpdate['state'] = 'normal'
        btnDelete['state'] = 'normal'
        btnAdd['state'] = 'disabled'
    elif state == 'Cancel':
        btnUpdate['state'] = 'disabled'
        btnDelete['state'] = 'disabled'
        btnAdd['state'] = 'disabled'
    else:
        btnUpdate['state'] = 'disabled'
        btnDelete['state'] = 'disabled'
        btnAdd['state'] = 'normal'


def load_edit_field_with_row_data(_tuple):
    if len(_tuple) == 0:
        return;

    id_value.set(_tuple[0]);
    arca_artist.delete(0, END)
    arca_artist.insert(0, _tuple[1])
    arca_title.delete(0, END)
    arca_title.insert(0, _tuple[2])
    arca_album.delete(0, END)
    arca_album.insert(0, _tuple[3])
    arca_year.delete(0, END)
    arca_year.insert(0, _tuple[4])
    arca_genre.delete(0, END)
    arca_genre.insert(0, _tuple[5])
    arca_bpm.delete(0, END)
    arca_bpm.insert(0, _tuple[6])
    arca_song_key.delete(0, END)
    arca_song_key.insert(0, _tuple[7])
    arca_rec_label.delete(0, END)
    arca_rec_label.insert(0, _tuple[8])
    arca_cat_no.delete(0, END)
    arca_cat_no.insert(0, _tuple[9])


def cancel():
    clear_all_fields()
    change_enabled_state('New')


def print_all_entries():
    global my_data_list

    for rec in my_data_list:
        print(rec)

    arca_artist.focus_set();


def add_entry():
    guid_value = id_value.get()
    artist = arca_artist.get()
    title = arca_title.get()
    album = arca_album.get()
    year = arca_year.get()
    genre = arca_genre.get()
    bpm = arca_bpm.get()
    song_key = arca_song_key.get()
    rec_label = arca_rec_label.get()
    catalog_no = arca_cat_no.get()

    if len(artist) == 0:
        change_background_color('#F2777A')
        return

    process_request(
        '_INSERT_',
        guid_value,
        artist,
        title,
        album,
        year,
        genre,
        bpm,
        song_key,
        rec_label,
        catalog_no
    )


def update_entry():
    guid_value = id_value.get()
    artist = arca_artist.get()
    title = arca_title.get()
    album = arca_album.get()
    year = arca_year.get()
    genre = arca_genre.get()
    bpm = arca_bpm.get()
    song_key = arca_song_key.get()
    rec_label = arca_rec_label.get()
    catalog_no = arca_cat_no.get()

    if len(artist) == 0:
        change_background_color('#F2777A')
        return

    process_request(
        '_UPDATE_',
        guid_value,
        artist,
        title,
        album,
        year,
        genre,
        bpm,
        song_key,
        rec_label,
        catalog_no
    )


def delete_entry():
    guid_value = id_value.get()
    process_request(
        '_DELETE_',
        guid_value,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


def process_request(
    command_type,
    guid_value,
    artist,
    title,
    album,
    year,
    genre,
    bpm,
    song_key,
    rec_label,
    catalog_no,):
    global my_data_list

    if command_type == '_UPDATE_':
        row = find_row_in_my_data_list(guid_value)
        if row >= 0:
            dict = {
                'id': guid_value,
                'artist': artist,
                'title': title,
                'album': album,
                'year': year,
                'genre': genre,
                'bpm': bpm,
                'song_key': song_key,
                'rec_label': rec_label,
                'catalog_no': catalog_no
            }
            my_data_list[row] = dict

    elif command_type == '_INSERT_':
        dict = {
            'id': guid_value,
            'artist': artist,
            'title': title,
            'album': album,
            'year': year,
            'genre': genre,
            'bpm': bpm,
            'song_key': song_key,
            'rec_label': rec_label,
            'catalog_no': catalog_no
        }
        my_data_list.append(dict)

    elif command_type == '_DELETE_':
        row = find_row_in_my_data_list(guid_value)
        if row >= 0:
            del my_data_list[row];

    save_json_to_file();
    load_trv_with_json();
    clear_all_fields();


def MouseButtonUpCallBack(event):
    currentRowIndex = trv.selection()[0]
    lastTuple = (trv.item(currentRowIndex, 'values'))
    load_edit_field_with_row_data(lastTuple)

    change_enabled_state('Edit')


trv.bind("<ButtonRelease>", MouseButtonUpCallBack)

ButtonFrame = LabelFrame(
    root,
    text='',
    bg='#D19A66',
    fg='#3E4451',
    font=(
        'SF Pro Display',
        16,
    )
)
ButtonFrame.grid(row=5, column=0, columnspan=6)

btnShow = Button(
    ButtonFrame,
    fg='#3E4451',
    font=(
        'SF Pro Display',
        14,
        'bold',
    ),
    text='Print',
    padx=20,
    pady=10,
    command=print_all_entries)
btnShow.pack(side=LEFT)

btnAdd = Button(
    ButtonFrame,
    fg='#3E4451',
    font=(
        'SF Pro Display',
        14,
        'bold',
    ),
    text='Add',
    padx=20,
    pady=10,
    command=add_entry)
btnAdd.pack(side=LEFT)

btnUpdate = Button(
    ButtonFrame,
    fg='#3E4451',
    font=(
        'SF Pro Display',
        14,
        'bold',
    ),
    text='Update',
    padx=20,
    pady=10,
    command=update_entry)
btnUpdate.pack(side=LEFT)

btnDelete = Button(
    ButtonFrame,
    fg='#3E4451',
    font=(
        'SF Pro Display',
        14,
        'bold',
    ),
    text='Delete',
    padx=20,
    pady=10,
    command=delete_entry)
btnDelete.pack(side=LEFT)

btnClear = Button(
    ButtonFrame,
    fg='#3E4451',
    font=(
        'SF Pro Display',
        14,
        'bold',
    ),
    text='Cancel',
    padx=18,
    pady=10,
    command=cancel)
btnClear.pack(side=LEFT)

btnExit = Button(
    ButtonFrame,
    fg='#3E4451',
    font=(
        'SF Pro Display',
        14,
        'bold',
    ),
    text='Exit',
    padx=20,
    pady=10,
    command=root.quit)
btnExit.pack(side=LEFT)

load_json_from_file()
load_trv_with_json()

arca_artist.focus_set();
root.mainloop()

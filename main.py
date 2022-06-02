import smtplib
import tkinter
from tkinter import messagebox


def send_email(email_entry, password_entry, to_email_entry, subject_entry, body_text):
    email = email_entry.get()
    to_email = to_email_entry.get()
    subject = subject_entry.get()
    message = f"""From: {email}
To: {to_email}
Subject: {subject}\n
{body_text.get(1.0, tkinter.END)}
"""
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.starttls()

    try:
        server.login(email, password_entry.get())
        server.sendmail(email, to_email, message)
        messagebox.showinfo(
            title='Email sent',
            message='Email successfully sent!'
        )
        email_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)
        to_email_entry.delete(0, tkinter.END)
        subject_entry.delete(0, tkinter.END)
        body_text.delete(1.0, tkinter.END)
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror(
            title='Authentication error',
            message='Failed to send email'
        )


def main():
    window = tkinter.Tk()
    window.title("Email Sender")

    # <a href="https://www.flaticon.com/free-icons/mail" title="mail icons">Mail icons created by Freepik - Flaticon</a>
    icon_image = tkinter.PhotoImage(file="images/email.png")

    window.iconphoto(True, icon_image)

    frame = tkinter.Frame(master=window)
    frame.pack(padx=20, pady=20)

    email_label = tkinter.Label(
        master=frame,
        text="Email: "
    )
    email_label.grid(row=0, column=0)
    email_entry = tkinter.Entry(
        master=frame,
        width=80,
        font=("Arial", 10)
    )
    email_entry.grid(row=0, column=1, pady=5)

    password_label = tkinter.Label(
        master=frame,
        text='Password: '
    )
    password_label.grid(row=1, column=0)
    password_entry = tkinter.Entry(
        master=frame,
        show="*",
        width=80,
        font=("Arial", 10)
    )
    password_entry.grid(row=1, column=1, pady=5)

    to_email_label = tkinter.Label(
        master=frame,
        text="Email to: "
    )
    to_email_label.grid(row=2, column=0)
    to_email_entry = tkinter.Entry(
        master=frame,
        width=80,
        font=("Arial", 10)
    )
    to_email_entry.grid(row=2, column=1, pady=5)

    subject_label = tkinter.Label(
        master=frame,
        text='Subject: '
    )
    subject_label.grid(row=3, column=0)
    subject_entry = tkinter.Entry(
        master=frame,
        width=80,
        font=("Arial", 10)
    )
    subject_entry.grid(row=3, column=1, pady=5)

    body_label = tkinter.Label(
        master=frame,
        text="Body: "
    )
    body_label.grid(row=4, column=0)
    body_text = tkinter.Text(
        master=frame
    )
    body_text.grid(row=5, column=1, padx=20)

    button = tkinter.Button(
        master=window,
        text="Send email",
        command=lambda: send_email(
            email_entry,
            password_entry,
            to_email_entry,
            subject_entry,
            body_text
        ),

    )
    button.pack(pady=20)

    tkinter.Label(window, text='This program only works with outlook').pack()

    window.mainloop()


if __name__ == '__main__':
    main()

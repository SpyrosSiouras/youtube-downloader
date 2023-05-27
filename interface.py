import flet as ft
from pytube import Search


# class TasksApp(ft.UserControl):
#     def build(self):
#         self.textField=ft.TextField(width=350)
#         self.addBtn   = ft.FloatingActionButton(icon= ft.icons.ADD,on_click= self.addClick)
#         self.tasks = ft.Column()
#         taskRow = ft.Column(controls=[
#                     ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                     controls=[self.textField, self.addBtn]),
#                     self.tasks])
#         return taskRow
    




def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()
 
    images = ft.Row(expand=1, wrap=False, scroll="always")

    page.add(images)



    s = Search("eminem without me")
    result_showing =10
    # print(s.results[0].title)
    lista =[]
    for x in range (result_showing):
        lista.append(s.results[x].thumbnail_url)

    for v in lista:
        if not v.endswith('.jpg'):
            v=v[:(v.find(".jpg")+4)]   
        print(v)           
        images.controls.append(
                ft.Image(                
                src=f"{v}",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),)
        )

    page.update()


ft.app(target=main)

import flet as ft

def main(page: ft.Page):

    # Route Change Handler
    def route_change(e):
        page.views.clear()

        # Home Page
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.Text("🏠 Home Page", size=30),
                        ft.ElevatedButton("Go to Profile", on_click=lambda e: page.go("/profile")),
                        ft.ElevatedButton("Go to Settings", on_click=lambda e: page.go("/settings"))
                    ]
                )
            )

        # Profile Page
        elif page.route == "/profile":
            page.views.append(
                ft.View(
                    "/profile",
                    [
                        ft.Text("👤 Profile Page", size=30),
                        ft.ElevatedButton("Back to Home", on_click=lambda e: page.go("/"))
                    ]
                )
            )

        # Settings Page
        elif page.route == "/settings":
            page.views.append(
                ft.View(
                    "/settings",
                    [
                        ft.Text("⚙️ Settings Page", size=30),
                        ft.ElevatedButton("Back to Home", on_click=lambda e: page.go("/"))
                    ]
                )
            )

        # Invalid Route (404)
        else:
            page.views.append(
                ft.View(
                    "/404",
                    [
                        ft.Text("❌ Page Not Found", size=30),
                        ft.ElevatedButton("Back to Home", on_click=lambda e: page.go("/"))
                    ]
                )
            )

        page.update()

    # Assign route handler
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)

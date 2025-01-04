import flet as ft
import time
import io
import sys

# Predefined sorting algorithms with their Big-O complexities
sorting_algorithms = {
    "Insertion Sort": {
        "code": '''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [38, 27, 43, 3, 9, 82, 10]
insertion_sort(arr)
print("Sorted array:", arr)
''',
        "big_o": "O(n^2)"
    },
    "Selection Sort": {
        "code": '''
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [38, 27, 43, 3, 9, 82, 10]
selection_sort(arr)
print("Sorted array:", arr)
''',
        "big_o": "O(n^2)"
    },
    "Bubble Sort": {
        "code": '''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [38, 27, 43, 3, 9, 82, 10]
bubble_sort(arr)
print("Sorted array:", arr)
''',
        "big_o": "O(n^2)"
    },
    "Linear Search": {
        "code": '''
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [38, 27, 43, 3, 9, 82, 10]
target = 9
result = linear_search(arr, target)
print("Element found at index:" if result != -1 else "Element not found", result)
''',
        "big_o": "O(n)"
    },
    "Binary Search": {
        "code": '''
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [3, 9, 10, 27, 38, 43, 82]  # Sorted array for binary search
target = 9
result = binary_search(arr, target)
print("Element found at index:" if result != -1 else "Element not found", result)
''',
        "big_o": "O(log n)"
    }
}


def main(page: ft.Page):
    page.title = "Python Sorting Algorithm Compiler"
    page.padding = 20
    page.scroll = "auto"
    page.theme_mode = "light"
    page.bgcolor="#6A1E55"
    page.horizontal_alignment="center"

    def load_code(e):
        """Load the selected algorithm's code into the code editor."""
        selected_algorithm = dropdown.value
        if selected_algorithm in sorting_algorithms:
            code_input.value = sorting_algorithms[selected_algorithm]["code"]
            code_input.update()

    def execute_code(e):
    
     output_text.value = ""  # Clear output
     code = code_input.value.strip()

     if not code:
        output_text.value = "No code to execute.\n"
        output_text.update()
        return

    # Redirect stdout to capture print statements
     old_stdout = sys.stdout
     sys.stdout = io.StringIO()

     try:
        start_time = time.time()  # Start measuring time
        exec(code)  # Execute the code
        runtime = time.time() - start_time  # Calculate runtime

        output = sys.stdout.getvalue()  # Get captured output
        output_text.value = output

        # Check if the executed code matches the selected algorithm
        selected_algorithm = dropdown.value
        if selected_algorithm in sorting_algorithms and code == sorting_algorithms[selected_algorithm]["code"].strip():
            big_o = sorting_algorithms[selected_algorithm]["big_o"]
            output_text.value += f"\nBig-O Complexity: {big_o}\n"

        output_text.value += f"Execution Time: {runtime:.4f} seconds\n"
     except Exception as ex:
        output_text.value = f"Error: {ex}\n"
     finally:
        sys.stdout = old_stdout
         
        output_text.update()


    def clear_fields(e):
        """Clear the input and output fields."""
        code_input.value = ""
        output_text.value = ""
        code_input.update()
        output_text.update()

    # Dropdown for selecting algorithms
    dropdown = ft.Dropdown(
        options=[ft.dropdown.Option(key, text=key) for key in sorting_algorithms.keys()],
        label="Select Sorting Algorithm",
        on_change=load_code,
    )

    # Code input area
    code_input = ft.TextField(
        label="Python Code",
        multiline=True,
        border=ft.InputBorder.NONE,
        width=600,
        expand=True,
        read_only=False
    )
    heading=ft.Container(col={"sm": 6},bgcolor='white',padding=20,border_radius=12,content=ft.Column(col={"sm": 6}, controls=[ft.Text("DSA Project",font_family="Times new roman",size="30")], horizontal_alignment="center",width="350"))
    div=ft.Divider()

    # Output display area
    output_text = ft.TextField(
        label="Output",
        multiline=True,
        border=ft.InputBorder.NONE,
        width=600,
        expand=True,
        read_only=True,
    )

    # Buttons
    execute_button = ft.FilledButton(
        "Run", width=80,
        style=ft.ButtonStyle(
            bgcolor="#A64D79",
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        on_click=execute_code
    )
    clear_button = ft.FilledButton(
        "Clear", width=100,
        style=ft.ButtonStyle(
            bgcolor="#A64D79",
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        on_click=clear_fields
    )

    # Layout
    page.add(
       heading,div,
        ft.ResponsiveRow([
            ft.Container(col={"sm": 6},bgcolor='white',padding=20,border_radius=12,content=ft.Column(col={"sm": 6}, controls=[dropdown],)),
            ft.Container(col={"sm": 6},bgcolor='white',padding=20,border_radius=12,content=ft.Column(col={"sm": 6}, controls=[execute_button],)),
            ft.Container(col={"sm": 6},bgcolor='white',padding=20,border_radius=12,content=ft.Column(col={"sm": 6}, controls=[code_input],)),
            ft.Container(col={"sm": 6},bgcolor='white',padding=20,border_radius=12,content=ft.Column(col={"sm": 6}, controls=[output_text, clear_button], horizontal_alignment="left"))
        ])
    )


ft.app(target=main)

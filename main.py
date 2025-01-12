from playwright.sync_api import sync_playwright
import os

user_song = input("Enter song's name: ")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    page.goto("https://music.apple.com/us/new")

    search_input = page.get_by_placeholder("Search")
    search_input.fill(user_song)

    page.wait_for_selector(".suggestion.svelte-11r59e8")  # Ensures the element is present
    first_element = page.locator(".suggestion.svelte-11r59e8").nth(0)
    first_element.click()

    page.screenshot(path="apple.png")
    os.system("start apple.png")

    name = input("Do you want to know the Artist name ? (yes/no): ").strip().lower()

    if name == "yes":
        artist_name_locator = page.locator(".top-search-lockup__primary__title").nth(1)
        artist_name = artist_name_locator.inner_text()

        print("Artist Name:", artist_name)

        info = input("Do you need more information about this artist ?")

        if info == "yes":

            page.goto("https://www.wikipedia.org/")
            search_input2 = page.locator('input#searchInput')
            search_input2.fill(artist_name)

            page.wait_for_selector(".suggestion-link")  # Ensures the element is present
            first_element = page.locator(".suggestion-link").nth(0)
            first_element.click()
            current_url = page.url
            print("Please click on the following link for further information", current_url)

        else:
            print("***Thank you for using the application***")





    else:
        print("***Thank you for using the application***")

    browser.close()

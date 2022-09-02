from bs4 import BeautifulSoup as BS


def edit_file(file, target, new_logos):
    with open(file, "r") as f:
        content = f.read()
        soup = BS(content,'html.parser')
        logos = soup.find_all('div', class_ = target)[0]
        for logo in new_logos:
            logos.append(BS(logo,'html.parser'))

    with open(file, "w") as f:
        f.write(soup.prettify())


def get_logo_html(logo_number, name, link):
    return f"""
    <div class="logo-box">
    <img src="assets/img/logo{logo_number}.png" alt="">

        <div class="info">
            <div class="content">
                <div class="icon">
                    <i class="fas fa-plus"></i>
                </div>

                <div class="entry">
                    <div>
                       <h5>{name}</h5>
                       <a style="text-decoration:none" href="{link}" target="_blank">{link[link.index('/') + 2:]}</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """

def main(files, target, logos_html):
    for file in files:
        edit_file(file, target, logos_html)


if __name__ == "__main__":
    files = ['about.html', 'index.html', 'index2.html']
    target = 'wapper-client'
    logos = []
    while True:
        stop = input("do you wanna add another logo (yes or no): ")
        if stop.strip() == "no":
            break
        number = input("enter logo image number: ")
        provider = input("enter the name of the company: ")
        link = input("enter the link of the company: ")
        if 'https://' not in link:
            link = input("link must start with https:// enter link again: ")
        logos.append((number, provider, link))
    logos_html = []
    for logo in logos:
        logos_html.append(get_logo_html(logo[0], logo[1], logo[2]))
    main(files, target, logos_html)
import requests

USERNAME = "khizer08"

user = requests.get(
    f"https://api.github.com/users/{USERNAME}"
).json()

repos = user["public_repos"]
followers = user["followers"]
following = user["following"]

svg = f"""
<svg width="900" height="250" xmlns="http://www.w3.org/2000/svg">

<style>
.bg {{
    fill:#1a1b26;
}}

.card {{
    fill:#24283b;
    stroke:#414868;
    stroke-width:2;
    rx:12;
}}

.title {{
    fill:#7aa2f7;
    font-size:28px;
    font-family:Arial;
    font-weight:bold;
}}

.label {{
    fill:#73daca;
    font-size:18px;
    font-family:Arial;
}}

.value {{
    fill:#bb9af7;
    font-size:36px;
    font-family:Arial;
    font-weight:bold;
}}
</style>

<rect width="900" height="250" class="bg"/>

<text x="450" y="40" text-anchor="middle" class="title">
🏆 GitHub Trophies
</text>

<rect x="20" y="70" width="190" height="140" class="card"/>
<rect x="240" y="70" width="190" height="140" class="card"/>
<rect x="460" y="70" width="190" height="140" class="card"/>
<rect x="680" y="70" width="190" height="140" class="card"/>

<text x="115" y="120" text-anchor="middle" class="value">{repos}</text>
<text x="115" y="160" text-anchor="middle" class="label">Repositories</text>

<text x="335" y="120" text-anchor="middle" class="value">{followers}</text>
<text x="335" y="160" text-anchor="middle" class="label">Followers</text>

<text x="555" y="120" text-anchor="middle" class="value">{following}</text>
<text x="555" y="160" text-anchor="middle" class="label">Following</text>

<text x="775" y="120" text-anchor="middle" class="value">ML</text>
<text x="775" y="160" text-anchor="middle" class="label">AI Enthusiast</text>

</svg>
"""

with open("trophy.svg", "w", encoding="utf-8") as f:
    f.write(svg)
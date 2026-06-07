import requests

USERNAME = "khizer08"

user = requests.get(
    f"https://api.github.com/users/{USERNAME}"
).json()

repos = user["public_repos"]
followers = user["followers"]

# Total Stars
stars = 0

repos_data = requests.get(
    f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
).json()

for repo in repos_data:
    stars += repo.get("stargazers_count", 0)

# Temporary values
# Later we can automate these too
streak = 108
contributions = 1027
active_days = 243

svg = f"""
<svg width="1120" height="280" xmlns="http://www.w3.org/2000/svg">

<style>
.bg {{
    fill:#1a1b26;
}}

.card {{
    fill:#24283b;
    stroke:#414868;
    stroke-width:2;
}}

.title {{
    fill:#7aa2f7;
    font-size:30px;
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
    font-size:38px;
    font-family:Arial;
    font-weight:bold;
}}

.line {{
    stroke:#414868;
    stroke-width:2;
}}
</style>

<rect width="1120" height="280" class="bg"/>

<line x1="120" y1="40" x2="300" y2="40" class="line"/>
<line x1="820" y1="40" x2="1000" y2="40" class="line"/>

<text x="560" y="52" text-anchor="middle" class="title">
🏆 GitHub Trophies
</text>

<!-- Stars -->
<rect x="20" y="90" width="170" height="140" rx="12" class="card"/>
<text x="105" y="145" text-anchor="middle" class="value">{stars}</text>
<text x="105" y="185" text-anchor="middle" class="label">⭐ Stars</text>

<!-- Repositories -->
<rect x="200" y="90" width="170" height="140" rx="12" class="card"/>
<text x="285" y="145" text-anchor="middle" class="value">{repos}</text>
<text x="285" y="185" text-anchor="middle" class="label">🚀 Repositories</text>

<!-- Followers -->
<rect x="380" y="90" width="170" height="140" rx="12" class="card"/>
<text x="465" y="145" text-anchor="middle" class="value">{followers}</text>
<text x="465" y="185" text-anchor="middle" class="label">👥 Followers</text>

<!-- Streak -->
<rect x="560" y="90" width="170" height="140" rx="12" class="card"/>
<text x="645" y="145" text-anchor="middle" class="value">{streak}</text>
<text x="645" y="185" text-anchor="middle" class="label">🔥 Streak</text>

<!-- Contributions -->
<rect x="740" y="90" width="170" height="140" rx="12" class="card"/>
<text x="825" y="145" text-anchor="middle" class="value">{contributions}</text>
<text x="825" y="185" text-anchor="middle" class="label">📈 Contributions</text>

<!-- Active Days -->
<rect x="920" y="90" width="170" height="140" rx="12" class="card"/>
<text x="1005" y="145" text-anchor="middle" class="value">{active_days}</text>
<text x="1005" y="185" text-anchor="middle" class="label">📅 Active Days</text>

</svg>
"""

with open("trophy.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("trophy.svg generated successfully")
python
import requests

USERNAME = "khizer08"

# -----------------------------
# Trophy Ranking Function
# -----------------------------
def trophies(value, low, medium):
    if value > medium:
        return "🏆🏆🏆"
    elif value >= low:
        return "🏆🏆"
    return "🏆"

# -----------------------------
# Fetch GitHub Data
# -----------------------------
user = requests.get(
    f"https://api.github.com/users/{USERNAME}"
).json()

repos = user.get("public_repos", 0)
followers = user.get("followers", 0)

# Total Stars
stars = 0

repos_data = requests.get(
    f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
).json()

for repo in repos_data:
    stars += repo.get("stargazers_count", 0)

# Temporary values
streak = 108
contributions = 1027
active_days = 243

# -----------------------------
# Trophy Levels
# -----------------------------
stars_trophy = trophies(stars, 5, 15)
repos_trophy = trophies(repos, 10, 20)
followers_trophy = trophies(followers, 10, 25)
streak_trophy = trophies(streak, 30, 100)
contrib_trophy = trophies(contributions, 500, 1000)
days_trophy = trophies(active_days, 100, 200)

# -----------------------------
# SVG
# -----------------------------
svg = f"""
<svg width="1200" height="320" xmlns="http://www.w3.org/2000/svg">

<style>
.bg {{
    fill:#1a1b26;
}}

.outer {{
    fill:none;
    stroke:#bb9af7;
    stroke-width:2;
}}

.card {{
    fill:#24283b;
    stroke:#565f89;
    stroke-width:2;
}}

.title {{
    fill:#7aa2f7;
    font-size:36px;
    font-family:Arial;
    font-weight:bold;
}}

.value {{
    fill:#bb9af7;
    font-size:42px;
    font-family:Arial;
    font-weight:bold;
}}

.label {{
    fill:#73daca;
    font-size:18px;
    font-family:Arial;
}}

.trophy {{
    fill:#fbbf24;
    font-size:22px;
    font-family:Arial;
    font-weight:bold;
}}
</style>

<rect width="1200" height="320" class="bg"/>

<rect x="10" y="10"
      width="1180"
      height="300"
      rx="20"
      class="outer"/>

<line x1="170" y1="50"
      x2="350" y2="50"
      stroke="#bb9af7"
      stroke-width="2"/>

<line x1="850" y1="50"
      x2="1030" y2="50"
      stroke="#bb9af7"
      stroke-width="2"/>

<text x="600"
      y="58"
      text-anchor="middle"
      class="title">
🏆 GitHub Trophies
</text>

<!-- Stars -->
<rect x="30" y="90" width="170" height="180" rx="15" class="card"/>
<text x="115" y="130" text-anchor="middle" class="trophy">{stars_trophy}</text>
<text x="115" y="200" text-anchor="middle" class="value">{stars}</text>
<text x="115" y="235" text-anchor="middle" class="label">Stars</text>

<!-- Repositories -->
<rect x="220" y="90" width="170" height="180" rx="15" class="card"/>
<text x="305" y="130" text-anchor="middle" class="trophy">{repos_trophy}</text>
<text x="305" y="200" text-anchor="middle" class="value">{repos}</text>
<text x="305" y="235" text-anchor="middle" class="label">Repositories</text>

<!-- Followers -->
<rect x="410" y="90" width="170" height="180" rx="15" class="card"/>
<text x="495" y="130" text-anchor="middle" class="trophy">{followers_trophy}</text>
<text x="495" y="200" text-anchor="middle" class="value">{followers}</text>
<text x="495" y="235" text-anchor="middle" class="label">Followers</text>

<!-- Streak -->
<rect x="600" y="90" width="170" height="180" rx="15" class="card"/>
<text x="685" y="130" text-anchor="middle" class="trophy">{streak_trophy}</text>
<text x="685" y="200" text-anchor="middle" class="value">{streak}</text>
<text x="685" y="235" text-anchor="middle" class="label">Streak</text>

<!-- Contributions -->
<rect x="790" y="90" width="170" height="180" rx="15" class="card"/>
<text x="875" y="130" text-anchor="middle" class="trophy">{contrib_trophy}</text>
<text x="875" y="200" text-anchor="middle" class="value">{contributions}</text>
<text x="875" y="235" text-anchor="middle" class="label">Contributions</text>

<!-- Active Days -->
<rect x="980" y="90" width="170" height="180" rx="15" class="card"/>
<text x="1065" y="130" text-anchor="middle" class="trophy">{days_trophy}</text>
<text x="1065" y="200" text-anchor="middle" class="value">{active_days}</text>
<text x="1065" y="235" text-anchor="middle" class="label">Active Days</text>

</svg>
"""

with open("trophy.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("trophy.svg generated successfully")

from kaggle_environments import make

env = make("orbit_wars", debug=True)

# Run agents here
env.run(["random", "random"])

html_output = env.render(mode="html")
with open("my_custom_match.html", "w") as f:
    f.write(html_output)

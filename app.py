from flask import Flask, render_template, request

app = Flask(__name__)

# Sample brand data (replace with your actual data)
brands = ["Brand A", "Brand B", "Brand C"]
locations = ["City 1", "City 2", "City 3"]

@app.route("/")
def index():
    selected_filter = request.args.get("filter")
    selected_value = request.args.get("selected")
    filtered_brands = brands.copy() if selected_filter != "brand" else []
    filtered_locations = locations.copy() if selected_filter != "location" else []

    if selected_value:
        if selected_filter == "brand":
            filtered_locations = [loc for loc in locations if loc in selected_value]
        else:
            filtered_brands = [brand for brand in brands if brand in selected_value]

    return render_template("index.html", brands=brands, locations=locations, 
                           selected_filter=selected_filter, selected_value=selected_value,
                           filtered_brands=filtered_brands, filtered_locations=filtered_locations)

if __name__ == "__main__":
    app.run(debug=True)

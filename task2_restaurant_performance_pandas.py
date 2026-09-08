import pandas as pd

# Create a food delivery dataset with 50 rows
df = pd.DataFrame({
    "restaurant_name": [
        "Spice Hub","Spice Hub","Spice Hub","Spice Hub","Spice Hub",
        "Spice Hub","Spice Hub","Spice Hub","Spice Hub","Spice Hub",
        "Pizza Point","Pizza Point","Pizza Point","Pizza Point","Pizza Point",
        "Pizza Point","Pizza Point","Pizza Point","Pizza Point","Pizza Point",
        "Curry House","Curry House","Curry House","Curry House","Curry House",
        "Curry House","Curry House","Curry House","Curry House","Curry House",
        "Dosa Corner","Dosa Corner","Dosa Corner","Dosa Corner","Dosa Corner",
        "Dosa Corner","Dosa Corner","Dosa Corner","Dosa Corner","Dosa Corner",
        "Biryani Palace","Biryani Palace","Biryani Palace","Biryani Palace","Biryani Palace",
        "Biryani Palace","Biryani Palace","Biryani Palace","Biryani Palace","Biryani Palace"
    ],
    "city": [
        "Chennai","Chennai","Mumbai","Delhi","Chennai","Mumbai","Delhi","Chennai","Mumbai","Delhi",
        "Chennai","Mumbai","Delhi","Chennai","Mumbai","Delhi","Chennai","Mumbai","Delhi","Chennai",
        "Mumbai","Delhi","Chennai","Mumbai","Delhi","Chennai","Mumbai","Delhi","Chennai","Mumbai",
        "Delhi","Chennai","Mumbai","Delhi","Chennai","Mumbai","Delhi","Chennai","Mumbai","Delhi",
        "Chennai","Mumbai","Delhi","Chennai","Mumbai","Delhi","Chennai","Mumbai","Delhi","Chennai"
    ],
    "order_value": [
        420,380,450,400,520,360,470,410,490,390,
        300,340,280,360,320,290,350,310,330,300,
        550,480,520,600,450,500,470,560,510,490,
        220,250,240,280,260,230,270,290,210,250,
        650,700,620,680,720,640,660,750,610,690
    ],
    "delivery_time_mins": [
        28,30,32,29,31,33,27,34,30,32,
        40,38,42,36,39,41,37,43,35,40,
        29,31,30,32,28,34,33,30,31,29,
        32,34,31,33,30,35,32,31,34,33,
        36,38,35,37,34,39,36,40,35,38
    ],
    "rating": [
        4.5,4.6,4.4,4.7,4.8,4.3,4.6,4.5,4.7,4.4,
        3.8,4.0,3.9,4.1,3.7,4.2,3.9,4.0,3.8,4.1,
        4.6,4.7,4.5,4.8,4.4,4.6,4.7,4.5,4.6,4.8,
        4.2,4.3,4.1,4.4,4.5,4.0,4.3,4.2,4.4,4.1,
        3.9,4.0,4.1,3.8,4.2,3.7,4.0,3.9,4.1,3.8
    ],
    "cuisine_type": [
        "Indian","Indian","Chinese","Indian","Indian","Chinese","Indian","Indian","Chinese","Indian",
        "Italian","Italian","Italian","Italian","Italian","Italian","Italian","Italian","Italian","Italian",
        "Indian","Indian","Indian","Indian","Indian","Indian","Indian","Indian","Indian","Indian",
        "South Indian","South Indian","South Indian","South Indian","South Indian","South Indian","South Indian","South Indian","South Indian","South Indian",
        "Indian","Indian","Indian","Indian","Indian","Indian","Indian","Indian","Indian","Indian"
    ]
})

# Required single method chain using groupby() and agg()
result = (
    df.groupby("restaurant_name")
      .agg(
          mean_order_value=("order_value", "mean"),
          mean_delivery_time=("delivery_time_mins", "mean"),
          mean_rating=("rating", "mean")
      )
      .query("mean_rating > 4.0 and mean_delivery_time < 35")
      .sort_values("mean_order_value", ascending=False)
      .reset_index()
)

print("Filtered and Ranked Restaurant Performance:")
print(result.to_string(index=False))

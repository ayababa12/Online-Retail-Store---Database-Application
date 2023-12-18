from flask import Flask,request,redirect, render_template, flash, session
from datetime import datetime
import psycopg2
import base64
app = Flask(__name__) #create instance of flask
app.secret_key = 'FOUR33'
conn = psycopg2.connect(
   database="FOUR3THREE", user='postgres', 
   password='----', host='127.0.0.1', port= '5432'
)



@app.route('/<category>', methods=['GET','POST'])
def products(category):
    cursor=conn.cursor()
    results_cloth=[]
    results_cos=[]
    product=[]
    pics=[]
    size=[]
    print(category)
    category_view=True
    categories=['coat','jackets',"blazers","shirts","t-shirts","sweatshirts","trousers","shoes","accessories","suits"]
    #display items according to category (upon clicking on the category's button)
    if category in categories:
        
        cursor.execute('SELECT distinct on (C1."clothing_name") C1."clothing_name",C2."clothing_price",C2."clothing_discount", "clothing_photos" from "Clothing/Accessory item name" as C2,"Clothing/Accessory item" as C1,"Photos Clothing" as Ph where C2."clothing_name"=C1."clothing_name" and C1."clothing_RefNb"=Ph."clothing_RefNb" and  C2."main_type"=%s',(category,))
        results_cloth=cursor.fetchall()
        print(results_cloth)
        for i in range(len(results_cloth)):
            results_cloth[i]=list(results_cloth[i])
            results_cloth[i][1]=round(results_cloth[i][1],2)
            results_cloth[i].append(round(results_cloth[i][1]/(1-results_cloth[i][2]),2)) # adding original price
            results_cloth[i][2]=results_cloth[i][2]*100
    elif category=='dresses-jumpsuits':
        category='dresses/jumpsuits'
        cursor.execute('SELECT distinct on (C1."clothing_name") C1."clothing_name",C2."clothing_price",C2."clothing_discount", "clothing_photos" from "Clothing/Accessory item name" as C2,"Clothing/Accessory item" as C1,"Photos Clothing" as Ph where C2."clothing_name"=C1."clothing_name" and C1."clothing_RefNb"=Ph."clothing_RefNb" and  C2."main_type"=%s',(category,))
        results_cloth=cursor.fetchall()
        print(results_cloth)
        for i in range(len(results_cloth)):
            results_cloth[i]=list(results_cloth[i])
            results_cloth[i][1]=round(results_cloth[i][1],2)
            results_cloth[i].append(round(results_cloth[i][1]/(1-results_cloth[i][2]),2)) # adding original price
            results_cloth[i][2]=results_cloth[i][2]*100
    elif category=='tops-bodysuits':
        category='tops/bodysuits'
        cursor.execute('SELECT distinct on (C1."clothing_name") C1."clothing_name",C2."clothing_price",C2."clothing_discount", "clothing_photos" from "Clothing/Accessory item name" as C2,"Clothing/Accessory item" as C1,"Photos Clothing" as Ph where C2."clothing_name"=C1."clothing_name" and C1."clothing_RefNb"=Ph."clothing_RefNb" and  C2."main_type"=%s',(category,))
        results_cloth=cursor.fetchall()
        print(results_cloth)
        for i in range(len(results_cloth)):
            results_cloth[i]=list(results_cloth[i])
            results_cloth[i][1]=round(results_cloth[i][1],2)
            results_cloth[i].append(round(results_cloth[i][1]/(1-results_cloth[i][2]),2)) # adding original price
            results_cloth[i][2]=results_cloth[i][2]*100
    elif category=='skirts-shorts':
        category='skirts/shorts'
        cursor.execute('SELECT distinct on (C1."clothing_name") C1."clothing_name",C2."clothing_price",C2."clothing_discount", "clothing_photos" from "Clothing/Accessory item name" as C2,"Clothing/Accessory item" as C1,"Photos Clothing" as Ph where C2."clothing_name"=C1."clothing_name" and C1."clothing_RefNb"=Ph."clothing_RefNb" and  C2."main_type"=%s',(category,))
        results_cloth=cursor.fetchall()
        print(results_cloth)
        for i in range(len(results_cloth)):
            results_cloth[i]=list(results_cloth[i])
            results_cloth[i][1]=round(results_cloth[i][1],2)
            results_cloth[i].append(round(results_cloth[i][1]/(1-results_cloth[i][2]),2)) # adding original price
            results_cloth[i][2]=results_cloth[i][2]*100
    elif category=='cosmetics':
        query='SELECT distinct on ("cosmetic_name") "cosmetic_name","cosmetic_price","cosmetic_discount", "cosmetic_photos" from "Cosmetic item" as i,"Photos Cosmetic" as p where i."cosmetic_RefNb"=p."cosmetic_RefNb"'
        cursor.execute(query)
        results_cos=cursor.fetchall()
        for i in range(len(results_cos)):
            results_cos[i]=list(results_cos[i])
            results_cos[i][1]=round(results_cos[i][1],2)
            results_cos[i].append(round(results_cos[i][1]/(1-results_cos[i][2]),2)) # adding original price
            results_cos[i][2]=results_cos[i][2]*100
    else: #no category button clicked
        category_view=False
        cursor.execute('(select "cosmetic_name","cosmetic_price","cosmetic_description","cosmetic_RefNb" from "Cosmetic item" where "cosmetic_name"='+"'"+category+"')")
        cosmetics=cursor.fetchall()
        cursor.execute('(select C1."clothing_name","clothing_price","clothing_description","clothing_RefNb","clothing_discount" from "Clothing/Accessory item" as C1, "Clothing/Accessory item name" as C2 where C1."clothing_name"=C2."clothing_name" and C1."clothing_name"='+"'"+category+"') union"+'(select "cosmetic_name","cosmetic_price","cosmetic_description","cosmetic_RefNb","cosmetic_discount" from "Cosmetic item" where "cosmetic_name"='+"'"+category+"')")
        product = list(cursor.fetchall()[0])
        product[1]=round(product[1],2)
        size=[]
        product.append(round(product[1]/(1-product[4]),2)) # adding original price
        product[4]=product[4]*100
        if len(cosmetics)==0:
            cursor.execute('select "size" from "Clothing/Accessory item" where "clothing_RefNb"='+"'"+str(product[3])+"'")
            size=cursor.fetchall()
            cursor.execute('(select * from "Photos Clothing" where "clothing_RefNb"='+str(product[3])+")")
        else:
            cursor.execute('select * from "Photos Cosmetic" where "cosmetic_RefNb"='+str(product[3]))
        pics=cursor.fetchall()
    search_query=request.form.get("search_bar")
    search_results_cloth=[]
    search_results_cos=[]
    ###################### Search 
    search=False
    if search_query!=None and search_query!='':
        category_view=False
        query='(SELECT distinct on (C1."clothing_name") C1."clothing_name",C2."clothing_price",C2."clothing_discount", "clothing_photos" from "Clothing/Accessory item name" as C2,"Clothing/Accessory item" as C1,"Photos Clothing" as Ph where C2."clothing_name"=C1."clothing_name" and C1."clothing_RefNb"=Ph."clothing_RefNb" and  (upper("main_type") like'+" upper('%"+search_query+"%') "+'or upper("sub_type") like '+"upper('%"+search_query+"%') "+'or upper("clothing_description") like '+"upper('%"+search_query+"%')"+' or upper(C1."clothing_name") like '+"upper('%"+search_query+"%')"+ "))" 
        cursor.execute(query)
        search_results_cloth=cursor.fetchall()
        query='(SELECT distinct on ("cosmetic_name") "cosmetic_name","cosmetic_price","cosmetic_discount", "cosmetic_photos" from "Cosmetic item" as i,"Photos Cosmetic" as p where i."cosmetic_RefNb"=p."cosmetic_RefNb" and (upper("cosmetic_name") like'+" upper('%"+search_query+"%')"+' or upper("cosmetic_description") like'+" upper('%"+search_query+"%')))"
        cursor.execute(query)
        search_results_cos=cursor.fetchall()
        for i in range(len(search_results_cloth)):
            search_results_cloth[i]=list(search_results_cloth[i])
            search_results_cloth[i][1]=round(search_results_cloth[i][1],2)
            search_results_cloth[i].append(round(search_results_cloth[i][1]/(1-search_results_cloth[i][2]),2)) # adding original price
            search_results_cloth[i][2]=search_results_cloth[i][2]*100
        for i in range(len(search_results_cos)):
            search_results_cos[i]=list(search_results_cos[i])
            search_results_cos[i][1]=round(search_results_cos[i][1],2)
            search_results_cos[i].append(round(search_results_cos[i][1]/(1-search_results_cos[i][2]),2)) # adding original price
            search_results_cos[i][2]=search_results_cos[i][2]*100
        search=True
        # Find the product with the specified ID
    
    return render_template('productdetail1.html',category=category,results_cloth=results_cloth,results_cos=results_cos,search=search,search_results_cloth=search_results_cloth,search_results_cos=search_results_cos,product=product,pics=pics,size=size,category_view=category_view)


    
@app.route("/", methods=['POST','GET']) 
def main():
    cursor=conn.cursor()
    ################### Discounted items
    query="""
        SELECT distinct on (c1."clothing_name") c1."clothing_name","clothing_price","clothing_discount","clothing_photos" 
        from "Clothing/Accessory item name" as c1,"Photos Clothing" as c2,"Clothing/Accessory item" as c3 where 
        c3."clothing_RefNb"=c2."clothing_RefNb" and c1."clothing_name"=c3."clothing_name"  
        and c3."clothing_RefNb" in (select "clothing_RefNb" from "Clothing/Accessory item" as ca1, "Clothing/Accessory item name" as ca2 where ca1."clothing_name"=ca2."clothing_name" order by "clothing_discount" desc limit 10)
        """
    cursor.execute(query)
    discounted_items=cursor.fetchall()
    for i in range(len(discounted_items)):
        discounted_items[i]=list(discounted_items[i])
        discounted_items[i][1]=round(discounted_items[i][1],2)
        discounted_items[i].append(round(discounted_items[i][1]/(1-discounted_items[i][2]),2)) # adding original price
        discounted_items[i][2]=discounted_items[i][2]*100
    discounted_items.sort(key=lambda T:T[2])
    discounted_items=discounted_items[::-1]
    query="""SELECT distinct on (C1."clothing_name") C1."clothing_name",C2."clothing_price",C2."clothing_discount", "clothing_photos" from "Clothing/Accessory item" as C1, "Clothing/Accessory item name" as C2,
            "Photos Clothing" as Ph where C1."clothing_name"=C2."clothing_name" and C1."clothing_RefNb"=Ph."clothing_RefNb"
            and C1."clothing_RefNb" in (select O."clothing_RefNb" from "Ordered By Clothing" as O group by(O."clothing_RefNb") order by(count(*)) desc);
            """
    ###################### Best Sellers
    cursor.execute(query)
    best_sellers=cursor.fetchall()

    for i in range(len(best_sellers)):
        best_sellers[i]=list(best_sellers[i])
        best_sellers[i][1]=round(best_sellers[i][1],2)
        best_sellers[i].append(round(best_sellers[i][1]/(1-best_sellers[i][2]),2)) # adding original price
        best_sellers[i][2]=best_sellers[i][2]*100
    search_query=request.form.get("search_bar")
    search_results_cloth=[]
    search_results_cos=[]
    ###################### Search 
    search=False
    if search_query!=None and search_query!='':
        query='(SELECT distinct on (C1."clothing_name") C1."clothing_name",C2."clothing_price",C2."clothing_discount", "clothing_photos" from "Clothing/Accessory item name" as C2,"Clothing/Accessory item" as C1,"Photos Clothing" as Ph where C2."clothing_name"=C1."clothing_name" and C1."clothing_RefNb"=Ph."clothing_RefNb" and  (upper("main_type") like'+" upper('%"+search_query+"%') "+'or upper("sub_type") like '+"upper('%"+search_query+"%') "+'or upper("clothing_description") like '+"upper('%"+search_query+"%')"+' or upper(C1."clothing_name") like '+"upper('%"+search_query+"%')"+ "))" 
        cursor.execute(query)
        search_results_cloth=cursor.fetchall()
        query='(SELECT distinct on ("cosmetic_name") "cosmetic_name","cosmetic_price","cosmetic_discount", "cosmetic_photos" from "Cosmetic item" as i,"Photos Cosmetic" as p where i."cosmetic_RefNb"=p."cosmetic_RefNb" and (upper("cosmetic_name") like'+" upper('%"+search_query+"%')"+' or upper("cosmetic_description") like'+" upper('%"+search_query+"%')))"
        cursor.execute(query)
        search_results_cos=cursor.fetchall()
        best_sellers=[]
        discounted_items=[]
        for i in range(len(search_results_cloth)):
            search_results_cloth[i]=list(search_results_cloth[i])
            search_results_cloth[i][1]=round(search_results_cloth[i][1],2)
            search_results_cloth[i].append(round(search_results_cloth[i][1]/(1-search_results_cloth[i][2]),2)) # adding original price
            search_results_cloth[i][2]=search_results_cloth[i][2]*100
        for i in range(len(search_results_cos)):
            search_results_cos[i]=list(search_results_cos[i])
            search_results_cos[i][1]=round(search_results_cos[i][1],2)
            search_results_cos[i].append(round(search_results_cos[i][1]/(1-search_results_cos[i][2]),2)) # adding original price
            search_results_cos[i][2]=search_results_cos[i][2]*100
        search=True
    ####################### cosmetics ads
    cursor.execute('select distinct on ("cosmetic_name") "cosmetic_name","cosmetic_price","cosmetic_discount","cosmetic_description","cosmetic_photos","Cosmetic item"."cosmetic_RefNb" from "Cosmetic item","Photos Cosmetic" where "Cosmetic item"."cosmetic_RefNb"="Photos Cosmetic"."cosmetic_RefNb" limit 8')
    cosmetics_ad=cursor.fetchall()
    for i in range(len(cosmetics_ad)):
        cosmetics_ad[i]=list(cosmetics_ad[i])
        cosmetics_ad[i][1]=round(cosmetics_ad[i][1],2)
        cosmetics_ad[i].append(round(cosmetics_ad[i][1]/(1-cosmetics_ad[i][2]),2))
        cosmetics_ad[i][2]=cosmetics_ad[i][2]*100
    
    return render_template("main1.html",discounted_items=discounted_items,
                           best_sellers=best_sellers,
                           search_results_cloth=search_results_cloth,search_results_cos=search_results_cos,search=search,cosmetics_ad=cosmetics_ad)


cart=[]
@app.route("/cart/addtocart/<product_name>", methods=['POST','GET']) 
def addToCart(product_name):
    
        cursor=conn.cursor()
        query = "SELECT ca.\"clothing_RefNb\" ,ca.clothing_name, cn.clothing_price FROM \"Clothing/Accessory item\" ca JOIN \"Clothing/Accessory item name\" cn ON ca.clothing_name = cn.clothing_name WHERE ca.clothing_name = %s;"
        cursor.execute(query, (product_name,))
        row = cursor.fetchone()

        if row:
            newitem = [
                 row[0],
                 row[1],
                 round(row[2]),
                 1
            ]

            for item in cart:
                if item[1]==product_name:
                    item[3]+=1
                    return redirect('/cart')
            
            cart.append(newitem)
            
        else:

            query = "SELECT \"cosmetic_RefNb\" ,cosmetic_name,cosmetic_price FROM \"Cosmetic item\" where cosmetic_name = %s;"
            cursor.execute(query, (product_name,))
            row = cursor.fetchone()

            if row:
                newitem = [
                    row[0],
                    row[1],
                    round(row[2]),
                    1
                ]

                for item in cart:
                    if item[1]==product_name:
                        item[3]+=1
                        return redirect('/cart')
                
                cart.append(newitem)

            else:
                print("Product Not Found!")


        return redirect('/cart')

# View cart
@app.route('/cart')
def view_cart():
    total = sum(int(item[2]) * int(item[3]) for item in cart)
    total=round(total)
    return render_template('cart.html',cart=cart ,total=total)

# Remove item from cart
@app.route('/cart/removefromcart/<product_name>',methods=['POST','GET'])
def remove_from_cart(product_name):
    for item in cart:
        if item[1]==product_name:
            cart.remove(item)
            break

    return render_template('cart.html')

@app.route('/cart/checkout',methods=['POST','GET'])
def checkout():
        try:
            if (len(cart)!=0):
                cursor= conn.cursor()
                for item in cart:

                    q1="SELECT * from \"Clothing/Accessory item\"  where clothing_name = %s "
                    cursor.execute(q1,(item[1],))
                    row= cursor.fetchone()
                    if row:
                        cursor.execute("""
                        INSERT INTO "Ordered By Clothing" ("clothing_RefNb", "customer_email", "status", "date_of_placement", "payment_method")
                        VALUES (%s, %s, %s, %s, %s)
                    """, (item[0], session['user_id'], 'completed', datetime.now(), 'cash'))
                        
                        
                    else:
                        cursor.execute("""
                        INSERT INTO "Ordered By Cosmetic" ("cosmetic_RefNb", "customer_email", "status", "date_of_placement", "payment_method")
                        VALUES (%s, %s, %s, %s, %s)
                    """, (item[0], session['user_id'], 'completed', datetime.now(), 'cash'))

                    conn.commit()
                cart.clear() 
        except:
            conn.rollback()
        return render_template('cart.html')


def user_exists(email):
    cursor = conn.cursor()
    query = 'SELECT * FROM "Customer" WHERE "customer_email" = %s'
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    return user is not None

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            email = request.form['email']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            gender = request.form['gender']
            address = request.form['address']
            phone_number = request.form['phone_number']
            date_of_birth = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d')
            credit_card = request.form['credit_card']
            password = request.form['password']

            if not email or '@' not in email or '.' not in email:
                flash('Invalid email address. Please enter a valid email.')
                return redirect('/signup')


            if user_exists(email):
                flash('User already exists. Please log in.')
                return redirect('/login')

            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO "Customer" ("customer_email","FName","LName", "gender", "address", "phonenumber", "DOB", "credit card","password")
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (email, first_name, last_name, gender, address, phone_number, date_of_birth, credit_card, password))

            conn.commit()

            flash('Signup successful! Please log in.')
            return redirect('/login')

        except Exception as e:
            print(f"Error during signup: {e}")
            flash('An error occurred during signup. Please try again.')
            conn.rollback()
            return redirect('/signup')

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            cursor = conn.cursor()
            cursor.execute('SELECT "password" FROM "Customer" WHERE "customer_email" = %s', (email,))
            conn.commit()
            user = cursor.fetchone()
            print(user)

            if password in user:  
                flash('Login successful!')
                user_logged_in = True
                session['user_logged_in'] = user_logged_in
                session['user_id'] = email
                return redirect("/")
            else:
                conn.rollback()
                flash('Invalid email or password. Please try again.')
        except:
            conn.rollback()
            flash('Invalid email or password. Please try again.')
    return render_template('login.html')

@app.route('/profile',methods=['GET', 'POST'])
def profile():
    print("Entered /profile route")
    cursor = conn.cursor()
    user_email = session['user_id']
    cursor.execute('SELECT * FROM "Customer" WHERE customer_email = %s', (user_email,))
    user_data = cursor.fetchone()
    if user_data:
        user_info = {
            'email': user_data[0],
            'first_name': user_data[1],
            'last_name': user_data[2],
            'password' : user_data[3],
            'gender': user_data[4],
            'address': user_data[5],
            'phonenumber': user_data[6],
            'credit_card': user_data[7],
            'date_of_birth': user_data[8],
            }
        query = """
        SELECT *
        FROM (
            SELECT *
            FROM "Ordered By Clothing"
            WHERE "customer_email" = %s
            AND "status" = %s
            ) AS subquery_alias
        ORDER BY subquery_alias.date_of_placement
        """
        cursor.execute(query, (session['user_id'], 'completed'))
        clothing_orders = cursor.fetchall()
        print(clothing_orders)
        query = """
            SELECT *
            FROM (
                SELECT * FROM "Ordered By Cosmetic"
                WHERE customer_email = %s
                AND "status" = %s
            ) AS subquery_alias
            ORDER BY subquery_alias.date_of_placement
        """
        cursor.execute(query, (session['user_id'], 'completed'))
        cosmetic_orders = cursor.fetchall()
        print(cosmetic_orders)
        clothing_order_details = {}
        for order in clothing_orders:
            date_of_placement = order[3] 
            if date_of_placement not in clothing_order_details:
                clothing_order_details[date_of_placement] = []

            cursor.execute('SELECT "clothing_name", "size" FROM "Clothing/Accessory item" WHERE  "clothing_RefNb" = %s', (order[0],))
            item_details = cursor.fetchone()
            clothing_order_details[date_of_placement].append(item_details)

        cosmetic_order_details = {}
        for order in cosmetic_orders:
            date_of_placement = order[3]  
            if date_of_placement not in cosmetic_order_details:
                cosmetic_order_details[date_of_placement] = []

            cursor.execute('SELECT "cosmetic_name" FROM "Cosmetic item"  WHERE "cosmetic_RefNb" = %s', (order[0],))
            item_details = cursor.fetchone()
            cosmetic_order_details[date_of_placement].append(item_details)
        return render_template('profile.html', user_info=user_info,clothing_order_details=clothing_order_details,cosmetic_order_details=cosmetic_order_details)


if __name__ == "__main__":
    app.run()

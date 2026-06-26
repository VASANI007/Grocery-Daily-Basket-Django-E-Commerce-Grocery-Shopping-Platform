import razorpay
from click import File
from django.conf import settings
from django.contrib import messages
from django.core.mail import *
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.core.mail import send_mail
from dd.models import *

from .utils import *


# Create your views here.
def indexpage(request):
    try:
        userid = request.session["log_id"]
        fetchdata = registermodel.objects.get(id=userid)
        context = {
            "rdata": fetchdata,
        }
    except:
        context = {}
    return render(request, "index.html", context)

def aboutpage(request):
    fetchcatdata = category.objects.all()
    try:
        userid = request.session["log_id"]
        fetchdata = registermodel.objects.get(id=userid)
        context = {
            # "data":fetchcatdata,
            "rdata":fetchdata,
            "cdata":fetchcatdata,
        }
        
    except:
        context ={
            "cdata":fetchcatdata,
        }
    return render(request,"about.html",context)

def addproductspage(request):
    fetchcatdata = category.objects.all()
    try:
        userid = request.session["log_id"]
        fetchdata = registermodel.objects.get(id=userid)
        context = {
            # "data":fetchcatdata,
            "rdata":fetchdata,
            "catdata":fetchcatdata,
        }
        
    except:
        context = {"catdata":fetchcatdata,}
    return render(request,"addproducts.html",context)

def blogpage(request):
    return render(request,"blog.html")

def blogsinglepage(request):
    return render(request,"blog-single.html")

def codespage(request):
    return render(request,"codes.html")

def contactpage(request):
    fetchcatdata = category.objects.all()
    try:
        userid = request.session["log_id"]
        fetchdata = registermodel.objects.get(id=userid)
        context = {
            # "data":fetchcatdata,
            "rdata":fetchdata,
            "cdata":fetchcatdata,
        }
        
    except:
        context ={
            "cdata":fetchcatdata,
        }
    if request.method == "POST":
        cname = request.POST.get("cname")
        cemail = request.POST.get("cemail")
        csubject = request.POST.get("csubject")
        cmsg = request.POST.get("cmsg")
        insert_query = contact(name=cname, email=cemail, subject=csubject, msg=cmsg)
        insert_query.save()
        # Send Email to the user
        email_subject = "Thank You for Contacting Us!"
        email_body = f"""
Dear {cname},
Thank you for contacting Daily Basket.
This is an automated response to confirm that we have successfully received your support request/ticket. Our support team is currently reviewing your query and will get back to you within 24 hours.
We appreciate your patience and understanding while we work to assist you as quickly as possible.
If you have any additional information related to your request, feel free to reply to this email.

Regards,
Daily Basket Team
Essentials Delivered Daily
        """

        try:
            # Styled HTML auto-reply to user
            html_user = f"""
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>Thank You — Daily Basket</title></head>
<body style="margin:0;padding:0;background:#f0f5f1;font-family:Arial,sans-serif;">
<div style="max-width:600px;margin:32px auto;border-radius:16px;overflow:hidden;box-shadow:0 8px 32px rgba(20,80,40,0.12);">
  <div style="background:#1a6b45;padding:36px 40px;text-align:center;">
    <div style="font-family:Georgia,serif;font-size:22px;color:#fff;font-weight:700;margin-bottom:4px;">
      &#128722; Daily <span style="color:#a8e6c4;">Basket</span>
    </div>
    <div style="font-size:11px;color:rgba(255,255,255,0.6);letter-spacing:1.5px;text-transform:uppercase;">Essentials Delivered Daily</div>
    <div style="font-size:42px;margin:18px 0 10px;">&#128231;</div>
    <h1 style="font-family:Georgia,serif;font-size:22px;color:#fff;font-weight:700;margin:0;">Message Received!</h1>
    <p style="color:rgba(255,255,255,0.75);font-size:13px;margin-top:6px;">We'll get back to you within 24 hours</p>
  </div>
  <div style="background:#fff;padding:32px 40px;">
    <p style="font-size:15px;color:#2d5a3d;font-weight:500;margin-bottom:8px;">Hello, {cname}! &#128075;</p>
    <p style="font-size:14px;color:#6b8c76;line-height:1.7;margin-bottom:24px;">
      Thank you for contacting <strong style="color:#1a6b45;">Daily Basket</strong>. We have successfully received your message and our support team is reviewing it.
    </p>
    <table cellpadding="0" cellspacing="0" border="0" width="100%"
           style="border:1px solid #d4edd9;border-radius:12px;background:#f5fbf7;margin-bottom:24px;">
      <tr>
        <td style="padding:12px 16px;border-bottom:1px solid #d4edd9;">
          <table width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128100; Name</td>
            <td style="text-align:right;font-size:13px;color:#1a3326;font-weight:600;">{cname}</td>
          </tr></table>
        </td>
      </tr>
      <tr>
        <td style="padding:12px 16px;border-bottom:1px solid #d4edd9;">
          <table width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128140; Subject</td>
            <td style="text-align:right;font-size:13px;color:#1a3326;font-weight:600;">{csubject}</td>
          </tr></table>
        </td>
      </tr>
      <tr>
        <td style="padding:12px 16px;">
          <table width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128172; Your Message</td>
          </tr><tr>
            <td style="font-size:13px;color:#2d4a36;padding-top:6px;line-height:1.6;">{cmsg}</td>
          </tr></table>
        </td>
      </tr>
    </table>
    <p style="font-size:12px;color:#8aab94;text-align:center;line-height:1.7;">
      If you have additional information, feel free to reply to this email.<br>
      This is an automated response — please do not reply directly.
    </p>
  </div>
  <div style="background:#f5fbf7;padding:24px 40px;text-align:center;border-top:1px solid #e4f0e7;">
    <div style="font-family:Georgia,serif;font-size:18px;color:#1a6b45;font-weight:700;margin-bottom:4px;">Daily <span style="color:#27ae60;">Basket</span> &#128722;</div>
    <p style="font-size:12px;color:#8aab94;">Essentials Delivered Daily &middot; Ahmedabad, Gujarat &middot; India</p>
    <div style="font-size:11px;color:#aabba8;margin-top:10px;">&copy; 2026 Daily Basket. All rights reserved.</div>
  </div>
</div>
</body></html>
            """
            user_email_obj = EmailMultiAlternatives(
                subject=email_subject,
                body=email_body,
                from_email=settings.EMAIL_HOST_USER,
                to=[cemail],
            )
            user_email_obj.attach_alternative(html_user, "text/html")
            user_email_obj.send(fail_silently=False)

            # Plain admin notification
            admin_subject = f"New Contact Query from {cname}: {csubject}"
            admin_body = f"New message from contact form.\n\nName: {cname}\nEmail: {cemail}\nSubject: {csubject}\n\nMessage:\n{cmsg}"
            send_mail(
                subject=admin_subject,
                message=admin_body,
                from_email=cemail,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent. Check your email!")
        except Exception as e:
            messages.error(request, f"Error sending email: {e}")

        return redirect("/")  # Redirect to the contact page after submission

    return render(request, "contact.html",context)


def faqpage(request):
    return render(request,"faq.html")

def homepage(request):
    fetchproducts = product.objects.all()
    fetchpcatdata = category.objects.all()
    try:
        userid = request.session["log_id"]
        fetchdata = registermodel.objects.get(id=userid)
        context = {
            # "data":fetchcatdata,
            "rdata":fetchdata,
            "products":fetchproducts,
            "pdata":fetchpcatdata,
        }
        
    except:
        context = {
            "products":fetchproducts,
            "pdata":fetchpcatdata,
        }
        
    return render(request,"home.html",context)

def masterpage(request):
    userid = request.session["log_id"]
    fetchdata = registermodel.objects.get(id=userid)
    print(fetchdata.u_image_url)
    context = {"rdata":fetchdata}
    
    return context

def indexd060page(request):
    return render(request,"indexd060.html")

def mailpage(request):
    return render(request,"mail.html")

def products1page(request):
    # Get sorting option from URL query parameters
    sort_option = request.GET.get('sort', 'default')
    search_query = request.GET.get('search', '')  # Capture search query
    
    # Fetch all categories
    fetchcatdata = category.objects.all()

    # Start with all products
    fetchproducts = product.objects.all()

    # Apply search query filtering
    if search_query:
        fetchproducts = fetchproducts.filter(p_name__icontains=search_query)

    # Apply sorting if provided
    if sort_option == "low_to_high":
        fetchproducts = fetchproducts.order_by('price')
    elif sort_option == "high_to_low":
        fetchproducts = fetchproducts.order_by('-price')

    # Debugging: print the number of products returned after filtering
    print("Search Query:", search_query)
    print("Products Count after search and sort:", fetchproducts.count())

    # Build the context with products, categories, selected sort option
    try:
        userid = request.session.get("log_id")
        fetchdata = registermodel.objects.get(id=userid)
        context = {
            "rdata": fetchdata,
            "products": fetchproducts,
            "data": fetchcatdata,
            "selected_sort": sort_option,
            "search_query": search_query,  # Pass search query to the template
        }
    except:
        context = {
            "products": fetchproducts,
            "data": fetchcatdata,
            "selected_sort": sort_option,
            "search_query": search_query,
        }

    return render(request, "products1.html", context)




def products2page(request):
    fetchproducts = product.objects.all()
    context ={
        "products":fetchproducts
    }
    return render(request,"products2.html",context)

def shortcodespage(request):
    return render(request,"shortcodes.html")

def singlepage(request, id):
    singledata = product.objects.get(id=id)
    fetchcatdata = category.objects.all()
    
    # Fetch reviews
    product_reviews = review.objects.filter(p_id=singledata).order_by('-id')
    total_reviews = product_reviews.count()
    avg_rating = 0
    
    star5 = product_reviews.filter(ratting=5).count()
    star4 = product_reviews.filter(ratting=4).count()
    star3 = product_reviews.filter(ratting=3).count()
    star2 = product_reviews.filter(ratting=2).count()
    star1 = product_reviews.filter(ratting=1).count()
    
    if total_reviews > 0:
        total_stars = (star5 * 5) + (star4 * 4) + (star3 * 3) + (star2 * 2) + (star1 * 1)
        avg_rating = round(total_stars / total_reviews, 1)

    try:
        userid = request.session["log_id"]
        fetchdata = registermodel.objects.get(id=userid)
        context = {
            "rdata": fetchdata,
            "data": singledata,
            "catdata": fetchcatdata,
            "reviews": product_reviews,
            "avg_rating": avg_rating,
            "total_reviews": total_reviews,
            "star5": star5, "star4": star4, "star3": star3, "star2": star2, "star1": star1,
        }
    except:
        context = {
            "data": singledata,
            "catdata": fetchcatdata,
            "reviews": product_reviews,
            "avg_rating": avg_rating,
            "total_reviews": total_reviews,
            "star5": star5, "star4": star4, "star3": star3, "star2": star2, "star1": star1,
        }
    return render(request,"single.html",context)



def fetchregisterdata(request):
    if request.method == "POST":
        name = request.POST.get("user")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        password = request.POST.get("password")
        role = request.POST.get("role")

        image = request.FILES["uimage"] if "uimage" in request.FILES else "photos/usericon.jpg"

        # Check if email or phone number already exists
        if registermodel.objects.filter(u_email=email).exists() or registermodel.objects.filter(u_phone=phone).exists():
            messages.error(request, "Email or phone number already registered. Please sign in.")
            return render(request, "index.html")  # Redirect back to index page with the error message

        # Insert data if unique
        insert_query = registermodel(
            u_name=name, u_email=email, u_phone=phone, u_address=address, 
            u_password=password, u_image=image, u_role=role
        )
        insert_query.save()

        messages.success(request, "Registration successful! You can now log in.")
        return render(request, "index.html")  # Redirect to index page with success message

    return render(request, "index.html")


def checklogindata(request):

    user = request.POST.get("user")
    phone = request.POST.get("phone")
    userpasseord = request.POST.get("password")

    try:
        userdata = registermodel.objects.get(u_phone=phone, u_password=userpasseord)
        print("success")

        #session

        request.session["log_id"] = userdata.id
        request.session["log_phone"] = userdata.u_phone
        request.session["log_name"] = userdata.u_name
        request.session["log_role"] = userdata.u_role
        request.session["log_email"] = userdata.u_email
        request.session["log_address"] = userdata.u_address


        print("session name:- ",request.session["log_name"])
        print("session name:- ",request.session["log_role"])
    except:
        print("failure")
        userdata = None

    if userdata is not None:
        return redirect("/")
    else:
        print("Invalid data")
        messages.error(request,"Invalid data")


    return render(request,"index.html")

def logout(request):
    try:
        
        del request.session["log_id"]
        del request.session["log_name"]
        del request.session["log_phone"]
        del request.session["log_email"]
        del request.session["log_address"]
        del request.session["log_role"]

    except:
        pass
    return redirect("/")

def categorypage(request, id):
    # Get sorting option and search query from request
    sort_option = request.GET.get('sort', 'default')  # Sorting option
    search_query = request.GET.get('search', '')  # Search query

    # Filter products by category and apply search query if provided
    fatchdata = product.objects.filter(cat_id=id)

    if search_query:
        fatchdata = fatchdata.filter(p_name__icontains=search_query)  # Search products by name

    # Apply sorting
    if sort_option == "low_to_high":
        fatchdata = fatchdata.order_by('price')
    elif sort_option == "high_to_low":
        fatchdata = fatchdata.order_by('-price')

    # Fetch all categories for sidebar navigation
    fatchcatdata = category.objects.all()

    # Check if user is logged in and fetch user data
    try:
        userid = request.session["log_id"]
        fetchdata = registermodel.objects.get(id=userid)
        context = {
            "rdata": fetchdata,
            "data": fatchdata,  # Sorted and filtered products
            "category": fatchcatdata,
            "selected_sort": sort_option,  # Pass selected sort to template
            "category_id": id,  # Pass category ID for URL handling
            "search_query": search_query,  # Pass search query to template
        }
    except:
        context = {
            "data": fatchdata,  # Sorted and filtered products
            "category": fatchcatdata,
            "selected_sort": sort_option,  # Pass selected sort to template
            "category_id": id,  # Pass category ID for URL handling
            "search_query": search_query,  # Pass search query to template
        }

    return render(request, "category.html", context)



def fetchproductdata(request):
    name = request.POST.get("pname")
    cat = request.POST.get("pcat")
    price = request.POST.get("productPrice")
    image = request.FILES["productImage"]
    images = request.FILES["backImage"]
    desc= request.POST.get("productDescription")
    status = request.POST.get("productStatus")

    sellerid = request.session["log_id"]

    insertquery = product(p_name=name,cat_id=category(id=cat),image=image,p_image=images,price=price,description=desc,in_stock=status,sellerid=registermodel(id=sellerid))
    insertquery.save()
    messages.success(request,"product add successfully!")
    print("register")
    return render(request,"addproducts.html")

def manageproductpage(request):
    sellerid_loggedin = request.session["log_id"]
    fetachdata = product.objects.filter(sellerid=sellerid_loggedin)
    fatchcatdata = category.objects.all()
    try:
        userid = request.session["log_id"]
        fetchdata = registermodel.objects.get(id=userid)
        context = {
            # "data":fetchcatdata,
            "rdata":fetchdata,
            "adata":fetachdata,
            "data": fatchcatdata,
        }
        
    except:
        context = {
            "adata":fetachdata,
            "data": fatchcatdata,
        }
    return render(request,"manageproduct.html",context)


def showcart(request):
    userid = request.session["log_id"]
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    fetchdata = cart.objects.filter(u_id=userid,orderstatus=1)
    amout = sum(item.totalamount for item in fetchdata)
    total = amout
    if total < 100:
        total += 29
    try:
        userid = request.session["log_id"]
        fetachdata = registermodel.objects.get(id=userid)
        context = {
            # "data":fetchcatdata,
            "rdata":fetachdata,
            "data":fetchdata,
            "total":total,
            "amout":amout,
            "days_of_week": days_of_week
        }
        
    except:
        context = {
            "data":fetchdata,
            "days_of_week": days_of_week
        }
    return render(request,"cart.html",context)

def manageorderpage(request):
    userid = request.session["log_id"]
    fetchdata = ordermodel.objects.filter(u_id=userid)
    try:
        userid = request.session["log_id"]
        fetachdata = registermodel.objects.get(id=userid)
        context = {
            # "data":fetchcatdata,
            "rdata":fetachdata,
            "data":fetchdata,
        }
        
    except:
        context = {
            "data":fetchdata,
        }
    return render(request,"manageorder.html",context)

def insertiontocart(request):
    pid = request.POST.get("pid")
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")

    userid = request.session["log_id"]
    totalamount = int(quantity) * float(price)

    try:
        fechdata = cart.objects.get(u_id=userid,p_id=pid,orderstatus=1)
    except:
        fechdata = None

    if fechdata is not None:
        fechdata.quantity += int(quantity)
        fechdata.totalamount += int(totalamount)
        fechdata.save()
    else:
        inserquery = cart(u_id=registermodel(id=userid),p_id=product(id=pid),quantity=quantity,totalamount=totalamount,orderstatus=1,orderid=0)
        inserquery.save()
    return redirect("/showcart")


def footerpage(request):
    fetchcatdata = category.objects.all()
    context ={
        "cdata":fetchcatdata,
    }
    return render(request,"footer.html",context)



def descrease(request,id):
    fechdata = cart.objects.get(id=id)
    if fechdata.quantity == 1:
        fechdata.delete()
    else:
        fechdata.quantity -= 1
        fechdata.totalamount -= fechdata.p_id.price
        fechdata.save()
    return redirect("/showcart")

def increase(request,id):
    fechdata = cart.objects.get(id=id)
    fechdata.quantity += 1
    fechdata.totalamount += fechdata.p_id.price
    fechdata.save()

    return redirect("/showcart")

def deleteitem(request,id):
    cart.objects.get(id=id).delete()
    return redirect("/showcart")

def deleteproduct(request,id):
    product.objects.get(id=id).delete()
    return redirect("/manageproduct")


from django.core.mail import EmailMultiAlternatives

def placeorder(request):
    userid = request.session["log_id"]
    user = registermodel.objects.get(id=userid)
    user_email = user.u_email

    cart_items = cart.objects.filter(u_id=userid, orderstatus=1)
    if not cart_items.exists():
        messages.error(request, "Your cart is empty. Please add items to place an order.")
        return redirect("/showcart")

    finaltotal = request.POST.get("total")
    phone = request.POST.get("phone")
    address = request.POST.get("address")
    payment = request.POST.get("payment")
    repeat_days = request.POST.getlist("repeat_days")
    repeat_days_str = ",".join(repeat_days)

    if not phone or not address:
        phone = user.u_phone
        address = user.u_address

    # ── Helper: HTML email build karo ──────────────────────────────────────
    def build_html_email(user, order_items_qs, lastid, finaltotal, payment, address, phone, repeat_days_str="", razorpay_id=None):

        # Product rows HTML (no images)
        rows_html = ""
        subtotal = 0.0
        for item in order_items_qs:
            rows_html += f"""
            <table cellpadding="0" cellspacing="0" border="0" width="100%"
                   style="border:1px solid #e4f0e7;border-radius:12px;margin-bottom:14px;background:#fafcfb;">
              <tr>
                <td style="padding:14px 16px;vertical-align:middle;">
                  <div style="font-size:14px;font-weight:600;color:#1a3326;margin-bottom:3px;">{item.p_id.p_name}</div>
                  <div style="font-size:12px;color:#7a9e87;">Qty: {item.quantity} &times; &#8377;{item.p_id.price}</div>
                </td>
                <td style="padding:14px 16px;vertical-align:middle;text-align:right;white-space:nowrap;">
                  <span style="font-size:15px;font-weight:700;color:#1a6b45;">&#8377;{item.totalamount}</span>
                </td>
              </tr>
            </table>
            """
            subtotal += float(item.totalamount)

        # Delivery calculation
        final_total_float = float(finaltotal)
        delivery_charge = final_total_float - subtotal
        if delivery_charge > 0:
            delivery_display = f"₹{delivery_charge:.2f}"
        else:
            delivery_display = "Free"

        # Delivery days display
        if repeat_days_str:
            days_display = repeat_days_str.replace(",", ", ")
        else:
            days_display = "Same Day Delivery"

        razorpay_row = (
            f'<tr><td style="color:#6b8c76;padding:6px 0;font-size:13px;">Razorpay Order ID</td>'
            f'<td style="text-align:right;font-size:13px;color:#1a3326;">{razorpay_id}</td></tr>'
            if razorpay_id else ""
        )

        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Order Confirmed — Daily Basket</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600&family=DM+Sans:wght@300;400;500&display=swap');
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:#f0f5f1; font-family:'DM Sans',sans-serif; color:#1a2e1f; }}
</style>
</head>
<body>
<div style="max-width:620px;margin:32px auto;border-radius:20px;overflow:hidden;
            box-shadow:0 8px 40px rgba(20,80,40,0.13);">

  <!-- HEADER -->
  <div style="background:#1a6b45;padding:40px 40px 32px;text-align:center;position:relative;">
    <div style="margin-bottom:20px;">
      <div style="font-family:Georgia,serif;font-size:24px;color:#fff;font-weight:700;">
      🛒  Daily <span style="color:#a8e6c4;">Basket</span>
      </div>
      <div style="font-size:12px;color:rgba(255,255,255,0.6);letter-spacing:1.5px;text-transform:uppercase;margin-top:4px;">
        Essentials Delivered Daily
      </div>
    </div>
    <div style="font-size:52px;margin:0 auto 12px;line-height:1;">&#9989;</div>
    <h1 style="font-family:Georgia,serif;font-size:26px;color:#fff;
               font-weight:700;margin-bottom:6px;">Order Confirmed! &#127881;</h1>
    <p style="color:rgba(255,255,255,0.75);font-size:14px;">Your order has been successfully placed</p>
    <div style="display:inline-block;background:rgba(255,255,255,0.12);color:#c8f0dc;
                font-size:12px;padding:5px 14px;border-radius:20px;margin-top:14px;
                border:1px solid rgba(255,255,255,0.2);">
      Order #{lastid}
    </div>
  </div>

  <!-- BODY -->
  <div style="background:#fff;padding:36px 40px;">

    <p style="font-size:16px;color:#2d5a3d;font-weight:500;margin-bottom:6px;">
      Hello, {user.u_name}! 👋
    </p>
    <p style="font-size:14px;color:#6b8c76;line-height:1.6;margin-bottom:28px;">
      We have received your order. We will deliver your fresh essentials soon.
      Below are the complete details of your order.
    </p>

    <!-- Summary Cards -->
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:28px;">
      <div style="background:#f5fbf7;border:1px solid #d4edd9;border-radius:12px;
                  padding:14px 16px;text-align:center;">
        <div style="font-size:11px;color:#6b8c76;text-transform:uppercase;
                    letter-spacing:0.8px;margin-bottom:5px;">Order ID</div>
        <div style="font-size:15px;font-weight:500;color:#1a4d2e;">#{lastid}</div>
      </div>
      <div style="background:#f5fbf7;border:1px solid #d4edd9;border-radius:12px;
                  padding:14px 16px;text-align:center;">
        <div style="font-size:11px;color:#6b8c76;text-transform:uppercase;
                    letter-spacing:0.8px;margin-bottom:5px;">Payment</div>
        <div style="font-size:15px;font-weight:500;color:#1a4d2e;">{payment}</div>
      </div>
      <div style="background:#f5fbf7;border:1px solid #d4edd9;border-radius:12px;
                  padding:14px 16px;text-align:center;">
        <div style="font-size:11px;color:#6b8c76;text-transform:uppercase;
                    letter-spacing:0.8px;margin-bottom:5px;">Total</div>
        <div style="font-size:18px;font-weight:600;color:#1a6b45;
                    font-family:'Playfair Display',serif;">₹{finaltotal}</div>
      </div>
    </div>

    <!-- Products -->
    <div style="font-size:13px;font-weight:500;color:#6b8c76;text-transform:uppercase;
                letter-spacing:1px;margin-bottom:14px;display:flex;align-items:center;gap:8px;">
      📦&nbsp; Order Items
      <span style="flex:1;height:1px;background:#e8f2eb;display:inline-block;"></span>
    </div>

    {rows_html}

    <!-- Price Summary -->
    <table style="width:100%;border-collapse:collapse;border-top:1px dashed #d4edd9;margin-top:10px;padding-top:14px;">
      <tr style="font-size:14px;color:#4a6a56;">
        <td style="padding:6px 0;">Subtotal</td>
        <td style="text-align:right;font-weight:500;padding:6px 0;">&#8377;{subtotal}</td>
      </tr>
      <tr style="font-size:14px;color:#4a6a56;">
        <td style="padding:6px 0 14px;">Delivery Charge</td>
        <td style="text-align:right;font-weight:500;padding:6px 0 14px;">{delivery_display}</td>
      </tr>
    </table>

    <!-- Grand Total -->
    <table style="width:100%;border-collapse:collapse;background:#1a6b45;border-radius:12px;margin:8px 0 28px;">
      <tr>
        <td style="padding:16px 20px;color:rgba(255,255,255,0.8);font-size:13px;font-family:Arial,sans-serif;">Grand Total</td>
        <td style="padding:16px 20px;text-align:right;color:#fff;font-size:24px;font-weight:700;font-family:Georgia,serif;letter-spacing:0.5px;">&#8377;{finaltotal}</td>
      </tr>
    </table>

    <!-- Delivery Details -->
    <div style="font-size:13px;font-weight:500;color:#6b8c76;text-transform:uppercase;
                letter-spacing:1px;margin-bottom:14px;">&#128203; Delivery Details</div>
    <table cellpadding="0" cellspacing="0" border="0" width="100%"
           style="margin-bottom:28px;border:1px solid #d4edd9;border-radius:12px;background:#f5fbf7;">
      <tr>
        <td style="padding:13px 16px;border-bottom:1px solid #d4edd9;vertical-align:middle;">
          <table cellpadding="0" cellspacing="0" border="0" width="100%">
            <tr>
              <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128205; Delivery Address</td>
              <td style="text-align:right;font-size:13px;color:#2d4a36;font-weight:500;">{address}</td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td style="padding:13px 16px;border-bottom:1px solid #d4edd9;vertical-align:middle;">
          <table cellpadding="0" cellspacing="0" border="0" width="100%">
            <tr>
              <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128222; Contact Number</td>
              <td style="text-align:right;font-size:13px;color:#2d4a36;font-weight:500;">{phone}</td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td style="padding:13px 16px;vertical-align:middle;">
          <table cellpadding="0" cellspacing="0" border="0" width="100%">
            <tr>
              <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128197; Delivery Days</td>
              <td style="text-align:right;font-size:13px;color:#1a6b45;font-weight:600;">{days_display}</td>
            </tr>
          </table>
        </td>
      </tr>
    </table>

    <!-- CTA Banner -->
    <div style="background:#1a6b45;border-radius:14px;padding:28px;
                text-align:center;margin-bottom:28px;position:relative;overflow:hidden;">
      <h3 style="font-family:'Playfair Display',serif;font-size:20px;
                 color:#fff;margin-bottom:8px;">Want to order again? 🛒</h3>
      <p style="font-size:13px;color:rgba(255,255,255,0.75);margin-bottom:18px;line-height:1.6;">
        We have daily fresh vegetables, dairy, fruits and much more available.<br>
        We fulfill your daily home needs — every day.
      </p>
      <a href="http://127.0.0.1:8000/"
         style="display:inline-block;background:#fff;color:#1a6b45;font-size:13px;
                font-weight:500;padding:11px 28px;border-radius:30px;text-decoration:none;">
        🛒 &nbsp; Shop Now
      </a>
    </div>

    <p style="font-size:12px;color:#8aab94;text-align:center;line-height:1.7;">
      If you have any questions, please contact us.<br>
      This is an automated email — please do not reply directly.
    </p>
  </div>
    
<!-- FOOTER -->
<div style="background:#f5fbf7;padding:34px 40px;text-align:center;
            border-top:1px solid #e4f0e7;">

    <!-- Thank You Text -->
    <h2 style="font-family:Georgia,serif;font-size:26px;
               color:#1a6b45;margin-bottom:12px;font-weight:700;">
        Thank You For Your Order 💚
    </h2>

    <p style="font-size:13px;color:#6b8c76;line-height:1.8;
              max-width:500px;margin:0 auto 24px;">
        We truly appreciate your trust in 
        <strong style="color:#1a6b45;">Daily Basket</strong>.  
        Your fresh essentials are being prepared with care and will be delivered soon.
    </p>

    <!-- Brand -->
    <div style="font-family:'Playfair Display',serif;font-size:22px;
                color:#1a6b45;font-weight:700;margin-bottom:8px;">
        Daily <span style="color:#27ae60;">Basket</span> 🛒
    </div>

    <p style="font-size:12px;color:#8aab94;line-height:1.8;margin-bottom:22px;">
        Essentials Delivered Daily <br>
        Ahmedabad, Gujarat · India
    </p>

    <!-- Button -->
    <a href="http://127.0.0.1:8000/"
       target="_blank"
       style="display:inline-block;background:#1a6b45;color:#ffffff;
              text-decoration:none;font-size:13px;font-weight:600;
              padding:12px 28px;border-radius:30px;margin-bottom:24px;">
        🛒 Continue Shopping
    </a>

    <!-- Copyright -->
    <div style="border-top:1px solid #dce9df;padding-top:18px;
                font-size:12px;color:#8aab94;line-height:1.7;">
        &copy; 2026 Daily Basket. All rights reserved.<br>
        Designed with 💚 by 
        <a href="http://127.0.0.1:8000/"
           target="_blank"
           style="color:#1a6b45;text-decoration:none;font-weight:600;">
            Daily Basket
        </a>
    </div>

</div>

</div>
</body>
</html>
        """
        return html

    # ── COD ────────────────────────────────────────────────────────────────
    if payment == "Cash on Delivery":
        storedata = ordermodel(
            u_id=user,
            finaltotal=finaltotal,
            phone=phone,
            address=address,
            paymode=payment,
            repeat_days=repeat_days_str,
            status=True,
        )
        storedata.save()
        lastid = storedata.id

        fetchdata = cart.objects.filter(u_id=userid, orderstatus=1)
        for i in fetchdata:
            i.orderstatus = 0
            i.orderid = lastid
            i.save()

        messages.success(request, "Order Placed Successfully")

        # HTML email bhejo
        html_body = build_html_email(user, fetchdata, lastid, finaltotal, payment, address, phone, repeat_days_str=repeat_days_str)
        email = EmailMultiAlternatives(
            subject=f"✅ Order Confirmed! #{lastid} — Daily Basket",
            body=f"Dear {user.u_name}, aapka order #{lastid} place ho gaya. Total: Rs. {finaltotal}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user_email],
        )
        email.attach_alternative(html_body, "text/html")
        email.send(fail_silently=False)

    # ── ONLINE / RAZORPAY ──────────────────────────────────────────────────
    else:
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))
        order_amount = int(float(finaltotal) * 100)
        razorpay_order = client.order.create({
            "amount": order_amount,
            "currency": "INR",
            "receipt": f"order_rcptid_{userid}",
            "payment_capture": "1",
        })

        storedata = ordermodel(
            u_id=user,
            finaltotal=finaltotal,
            phone=phone,
            address=address,
            paymode="Online",
            razorpay_order_id=razorpay_order['id'],
            repeat_days=repeat_days_str,
            status=True,
        )
        storedata.save()
        lastid = storedata.id

        cart_items = cart.objects.filter(u_id=userid, orderstatus=1)
        for item in cart_items:
            item.orderstatus = 0
            item.orderid = lastid
            item.save()

        # HTML email bhejo
        html_body = build_html_email(
            user, cart_items, lastid, finaltotal,
            "Online Payment (Razorpay)", address, phone,
            repeat_days_str=repeat_days_str,
            razorpay_id=razorpay_order['id']
        )
        email = EmailMultiAlternatives(
            subject=f"✅ Order Confirmed! #{lastid} — Daily Basket",
            body=f"Dear {user.u_name}, aapka order #{lastid} place ho gaya. Total: Rs. {finaltotal}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user_email],
        )
        email.attach_alternative(html_body, "text/html")
        email.send(fail_silently=False)

        request.session['razorpay_order_id'] = razorpay_order['id']
        request.session['order_amount'] = order_amount
        request.session['current_order_id'] = lastid

        return redirect("/payment")

    return redirect("/")

def payment_page(request):
    try:
        userid = request.session["log_id"]
        fetchdata = registermodel.objects.get(id=userid)
    except:
        fetchdata = None
        
    context = {
        "razorpay_order_id": request.session.get('razorpay_order_id'),
        "amount": request.session.get('order_amount'),
        "key": settings.RAZORPAY_KEY_ID,
        "currency": "INR",
        "order_id": request.session.get('current_order_id'),
        "rdata": fetchdata,
    }
    return render(request, "payment.html", context)



def payment_success(request):
    return redirect("/")


def showwish(request):
    if "log_id" not in request.session:
        return redirect("/login")  # Redirect if user is not logged in

    user_id = request.session["log_id"]

    if request.method == "POST":
        pid = request.POST.get("pid")  # Product ID from form
        if pid:
            product_obj = product.objects.get(id=pid)

            # Check if the item is already in the wishlist to avoid duplicates
            if not wishlist.objects.filter(u_id=user_id, p_id=product_obj).exists():
                wishlist.objects.create(u_id_id=user_id, p_id=product_obj)
                messages.success(request, "Item added to wishlist!")
            else:
                messages.info(request, "Item is already in your wishlist.")

    # Fetch wishlist items
    fetchdata = wishlist.objects.filter(u_id=user_id)

    try:
        user_data = registermodel.objects.get(id=user_id)
        context = {
            "rdata": user_data,
            "data": fetchdata,
        }
    except registermodel.DoesNotExist:
        context = {"data": fetchdata}

    return render(request, "wish.html", context)

def deletewish(request,id):
    wishlist.objects.get(id=id).delete()
    return redirect("/showwish")

 # Import your custom model


def change_password(request):
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        print("current", current_password)
        print("new password", new_password)
        print("confirm password", confirm_password)

        # Ensure session contains user ID
        userid = request.session.get("log_id")

        # Fetch user data
        try:
            fetachdata = registermodel.objects.get(id=userid)
        except registermodel.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect("/")

        # Check if current password is correct
        if fetachdata.u_password != current_password:
            messages.error(request, "Current password is incorrect.")
            return redirect("/")

        # Check if new passwords match
        if new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return redirect("/")

        # Change password securely
        fetachdata.u_password = new_password  # You should hash this in production!
        fetachdata.save()

        # Send styled HTML confirmation email
        html_pwd = f"""
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>Password Updated — Daily Basket</title></head>
<body style="margin:0;padding:0;background:#f0f5f1;font-family:Arial,sans-serif;">
<div style="max-width:600px;margin:32px auto;border-radius:16px;overflow:hidden;box-shadow:0 8px 32px rgba(20,80,40,0.12);">
  <div style="background:#1a6b45;padding:36px 40px;text-align:center;">
    <div style="font-family:Georgia,serif;font-size:22px;color:#fff;font-weight:700;margin-bottom:4px;">
      &#128722; Daily <span style="color:#a8e6c4;">Basket</span>
    </div>
    <div style="font-size:11px;color:rgba(255,255,255,0.6);letter-spacing:1.5px;text-transform:uppercase;">Essentials Delivered Daily</div>
    <div style="font-size:42px;margin:18px 0 10px;">&#128274;</div>
    <h1 style="font-family:Georgia,serif;font-size:22px;color:#fff;font-weight:700;margin:0;">Password Updated</h1>
    <p style="color:rgba(255,255,255,0.75);font-size:13px;margin-top:6px;">Your account is secure</p>
  </div>
  <div style="background:#fff;padding:32px 40px;">
    <p style="font-size:15px;color:#2d5a3d;font-weight:500;margin-bottom:8px;">Hello, {fetachdata.u_name}! &#128075;</p>
    <p style="font-size:14px;color:#6b8c76;line-height:1.7;margin-bottom:24px;">
      Your <strong style="color:#1a6b45;">Daily Basket</strong> account password has been successfully updated.
      If you did not make this change, please contact us immediately.
    </p>
    <table cellpadding="0" cellspacing="0" border="0" width="100%"
           style="border:1px solid #d4edd9;border-radius:12px;background:#f5fbf7;margin-bottom:24px;">
      <tr>
        <td style="padding:12px 16px;border-bottom:1px solid #d4edd9;">
          <table width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128100; Account Name</td>
            <td style="text-align:right;font-size:13px;color:#1a3326;font-weight:600;">{fetachdata.u_name}</td>
          </tr></table>
        </td>
      </tr>
      <tr>
        <td style="padding:12px 16px;border-bottom:1px solid #d4edd9;">
          <table width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128274; New Password</td>
            <td style="text-align:right;font-size:13px;color:#1a6b45;font-weight:700;letter-spacing:1px;">{new_password}</td>
          </tr></table>
        </td>
      </tr>
      <tr>
        <td style="padding:12px 16px;">
          <table width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#9989; Status</td>
            <td style="text-align:right;font-size:13px;color:#1a6b45;font-weight:700;">Password Changed Successfully</td>
          </tr></table>
        </td>
      </tr>
    </table>
    <p style="font-size:12px;color:#8aab94;text-align:center;line-height:1.7;">
      If you did not request this change, contact support immediately.<br>
      This is an automated email — please do not reply directly.
    </p>
  </div>
  <div style="background:#f5fbf7;padding:24px 40px;text-align:center;border-top:1px solid #e4f0e7;">
    <div style="font-family:Georgia,serif;font-size:18px;color:#1a6b45;font-weight:700;margin-bottom:4px;">Daily <span style="color:#27ae60;">Basket</span> &#128722;</div>
    <p style="font-size:12px;color:#8aab94;">Essentials Delivered Daily &middot; Ahmedabad, Gujarat &middot; India</p>
    <div style="font-size:11px;color:#aabba8;margin-top:10px;">&copy; 2026 Daily Basket. All rights reserved.</div>
  </div>
</div>
</body></html>
        """
        pwd_email = EmailMultiAlternatives(
            subject='🔏 Your Password Has Been Updated — Daily Basket',
            body=f'Hello {fetachdata.u_name}, your Daily Basket password has been updated successfully.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[fetachdata.u_email],
        )
        pwd_email.attach_alternative(html_pwd, "text/html")
        pwd_email.send(fail_silently=False)

        messages.success(request, "Your password has been changed successfully!")
        return redirect("/")

    return render(request, "index.html")




def cancelorder(request,id):
    fatchdata = ordermodel.objects.get(id=id)
    fatchdata.status = False
    fatchdata.save()
    messages.success(request,"Your order is cancelled")
    return redirect("/manageorder")

def abortpayment(request, id):
    # Restore cart items back to cart
    cart_items = cart.objects.filter(orderid=id)
    for item in cart_items:
        item.orderstatus = 1
        item.orderid = 0
        item.save()
        
    # Delete the incomplete order
    ordermodel.objects.filter(id=id).delete()
    
    messages.warning(request, "Payment cancelled. Items restored to your cart.")
    return redirect("/showcart")

def yourorderdetailes(request, id):
    fachdata = cart.objects.filter(orderid=id)
    amout = sum(item.totalamount for item in fachdata)
    totalamount = amout if amout >= 100 else amout + 29
    fetchcatdata = category.objects.all()

    context = {
        "data": fachdata,
        "amout": amout,
        "totalamount": totalamount,
        "catdata": fetchcatdata,
    }
    userid = request.session.get("log_id")
    reviewed_product_ids = []
    if userid:
        try:
            fetchdata = registermodel.objects.get(id=userid)
            context["rdata"] = fetchdata
            product_ids = [item.p_id.id for item in fachdata]
            reviewed_product_ids = list(review.objects.filter(u_id=fetchdata, p_id_id__in=product_ids).values_list('p_id_id', flat=True))
        except registermodel.DoesNotExist:
            pass
    context["reviewed_product_ids"] = reviewed_product_ids

    return render(request, "yourorderdetailes.html", context)

def sellerorder(request):
    userid = request.session.get("log_id")
    context = {}
    try:
        user_data = registermodel.objects.get(id=userid)
        context["rdata"] = user_data
    except registermodel.DoesNotExist:
        pass

    seller_id = request.session.get("log_id")

    # Step 1: Get seller's products
    seller_products = product.objects.filter(sellerid=seller_id)

    # Step 2: Get all cart entries where products are from this seller and order is placed
    seller_carts = cart.objects.filter(p_id__in=seller_products, orderstatus=0).select_related('p_id', 'u_id')

    final_data = []

    # Step 3: For each cart item, get order details
    for c in seller_carts:
        try:
            order = ordermodel.objects.get(id=c.orderid)
            final_data.append({
                'product_name': c.p_id.p_name,
                'product_image': c.p_id.image.url if c.p_id.image else '',
                'quantity': c.quantity,
                'totalamount': c.totalamount,
                'username': c.u_id.u_name,
                'paymode': order.paymode,
                'timestamp': order.timestamp
            })
        except ordermodel.DoesNotExist:
            continue

    # Add order data to context
    context["orders"] = final_data

    return render(request, "sellerorders.html", context)


def editproductdata(request, product_id):
    prod = get_object_or_404(product, id=product_id)
    fetchcatdata = category.objects.all()

    context = {
        "productid": product_id,
        "product": prod,
        "catdata": fetchcatdata,
    }

    try:
        userid = request.session["log_id"]
        fetchdata = registermodel.objects.get(id=userid)
        context["rdata"] = fetchdata
    except registermodel.DoesNotExist:
        pass

    if request.method == "POST":
        name = request.POST.get("pname")
        cat_id = request.POST.get("pcat")
        price = request.POST.get("productPrice")
        image = request.FILES.get("productImage")
        back_image = request.FILES.get("backImage")
        desc = request.POST.get("productDescription")
        status = request.POST.get("productStatus")

        # Update fields
        prod.p_name = name
        prod.cat_id = category.objects.get(id=cat_id)
        prod.price = price
        prod.description = desc
        prod.in_stock = status

        if image:
            prod.image = image
        if back_image:
            prod.p_image = back_image

        prod.save()
        messages.success(request, "Product updated successfully!")
        return redirect(manageproductpage)  # use quotes if it's a URL name

    return render(request, "editproducts.html", context)



def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = registermodel.objects.get(u_email=email)

            # Send account info email (does NOT change the password)
            html_rst = f"""
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>Account Info — Daily Basket</title></head>
<body style="margin:0;padding:0;background:#f0f5f1;font-family:Arial,sans-serif;">
<div style="max-width:600px;margin:32px auto;border-radius:16px;overflow:hidden;box-shadow:0 8px 32px rgba(20,80,40,0.12);">
  <div style="background:#1a6b45;padding:36px 40px;text-align:center;">
    <div style="font-family:Georgia,serif;font-size:22px;color:#fff;font-weight:700;margin-bottom:4px;">
      &#128722; Daily <span style="color:#a8e6c4;">Basket</span>
    </div>
    <div style="font-size:11px;color:rgba(255,255,255,0.6);letter-spacing:1.5px;text-transform:uppercase;">Essentials Delivered Daily</div>
    <div style="font-size:42px;margin:18px 0 10px;">&#128272;</div>
    <h1 style="font-family:Georgia,serif;font-size:22px;color:#fff;font-weight:700;margin:0;">Your Account Details</h1>
    <p style="color:rgba(255,255,255,0.75);font-size:13px;margin-top:6px;">As requested, here is your account information</p>
  </div>
  <div style="background:#fff;padding:32px 40px;">
    <p style="font-size:15px;color:#2d5a3d;font-weight:500;margin-bottom:8px;">Hello, {user.u_name}! &#128075;</p>
    <p style="font-size:14px;color:#6b8c76;line-height:1.7;margin-bottom:24px;">
      You requested your account details for <strong style="color:#1a6b45;">Daily Basket</strong>.
      Here is all your account information:
    </p>
    <table cellpadding="0" cellspacing="0" border="0" width="100%"
           style="border:1px solid #d4edd9;border-radius:12px;background:#f5fbf7;margin-bottom:24px;">
      <tr>
        <td style="padding:12px 16px;border-bottom:1px solid #d4edd9;">
          <table width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128100; Name</td>
            <td style="text-align:right;font-size:13px;color:#1a3326;font-weight:600;">{user.u_name}</td>
          </tr></table>
        </td>
      </tr>
      <tr>
        <td style="padding:12px 16px;border-bottom:1px solid #d4edd9;">
          <table width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128231; Email</td>
            <td style="text-align:right;font-size:13px;color:#1a3326;font-weight:600;">{user.u_email}</td>
          </tr></table>
        </td>
      </tr>
      <tr>
        <td style="padding:12px 16px;border-bottom:1px solid #d4edd9;">
          <table width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128222; Phone</td>
            <td style="text-align:right;font-size:13px;color:#1a3326;font-weight:600;">{user.u_phone}</td>
          </tr></table>
        </td>
      </tr>
      <tr>
        <td style="padding:12px 16px;">
          <table width="100%" cellpadding="0" cellspacing="0"><tr>
            <td style="font-size:12px;color:#6b8c76;font-weight:500;">&#128274; Password</td>
            <td style="text-align:right;font-size:13px;color:#1a6b45;font-weight:700;letter-spacing:1px;">{user.u_password}</td>
          </tr></table>
        </td>
      </tr>
    </table>
    <p style="font-size:12px;color:#8aab94;text-align:center;line-height:1.7;">
      If you did not request this, please contact support immediately.<br>
      This is an automated email — please do not reply directly.
    </p>
  </div>
  <div style="background:#f5fbf7;padding:24px 40px;text-align:center;border-top:1px solid #e4f0e7;">
    <div style="font-family:Georgia,serif;font-size:18px;color:#1a6b45;font-weight:700;margin-bottom:4px;">Daily <span style="color:#27ae60;">Basket</span> &#128722;</div>
    <p style="font-size:12px;color:#8aab94;">Essentials Delivered Daily &middot; Ahmedabad, Gujarat &middot; India</p>
    <div style="font-size:11px;color:#aabba8;margin-top:10px;">&copy; 2026 Daily Basket. All rights reserved.</div>
  </div>
</div>
</body></html>
            """
            rst_email = EmailMultiAlternatives(
                subject='👤 Your Account Information — Daily Basket',
                body=f'Hello {user.u_name}, your Daily Basket account info: Name: {user.u_name}, Email: {user.u_email}, Phone: {user.u_phone}, Password: {user.u_password}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )
            rst_email.attach_alternative(html_rst, "text/html")
            rst_email.send(fail_silently=False)

            messages.success(request, "Account details sent to your email! Please check your inbox.")
        except registermodel.DoesNotExist:
            messages.error(request, "No account found with this email address.")

        return redirect('/index')


def submit_review(request, id):
    if "log_id" not in request.session:
        return redirect("/")
    
    if request.method == "POST":
        userid = request.session["log_id"]
        prod = product.objects.get(id=id)
        user = registermodel.objects.get(id=userid)
        
        # Check if already reviewed
        if review.objects.filter(u_id=user, p_id=prod).exists():
            messages.error(request, "You have already reviewed this product!")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        rating = request.POST.get("rating")
        review_text = request.POST.get("review_text")
        review_image = request.FILES.get("review_image")
        
        # Save review
        new_review = review(
            u_id=user,
            p_id=prod,
            ratting=rating,
            review=review_text,
            image=review_image
        )
        new_review.save()
        messages.success(request, "Your review has been submitted successfully!")
        
    return redirect(request.META.get('HTTP_REFERER', '/'))

def my_reviews(request):
    if "log_id" not in request.session:
        return redirect("/")
        
    userid = request.session["log_id"]
    user = registermodel.objects.get(id=userid)
    user_reviews = review.objects.filter(u_id=user)
    
    context = {
        "rdata": user,
        "reviews": user_reviews
    }
    return render(request, "my_reviews.html", context)

def edit_review(request, id):
    if "log_id" not in request.session:
        return redirect("/")
        
    if request.method == "POST":
        userid = request.session["log_id"]
        rating = request.POST.get("rating")
        review_text = request.POST.get("review_text")
        review_image = request.FILES.get("review_image")
        
        try:
            rev = review.objects.get(id=id, u_id__id=userid)
            rev.ratting = rating
            rev.review = review_text
            if review_image:
                rev.image = review_image
            rev.save()
            messages.success(request, "Your review has been updated successfully!")
        except review.DoesNotExist:
            messages.error(request, "Review not found!")
            
    return redirect("/my_reviews")

def delete_review(request, id):
    if "log_id" not in request.session:
        return redirect("/")
        
    userid = request.session["log_id"]
    try:
        rev = review.objects.get(id=id, u_id__id=userid)
        rev.delete()
        messages.success(request, "Review deleted successfully!")
    except review.DoesNotExist:
        messages.error(request, "Review not found!")
        
    return redirect("/my_reviews")

def update_profile_image(request):
    if "log_id" not in request.session:
        return redirect("/")
        
    if request.method == "POST" and request.FILES.get("u_image"):
        userid = request.session["log_id"]
        try:
            user = registermodel.objects.get(id=userid)
            user.u_image = request.FILES["u_image"]
            user.save()
            messages.success(request, "Profile image updated successfully!")
        except registermodel.DoesNotExist:
            messages.error(request, "User not found.")
            
    return redirect(request.META.get('HTTP_REFERER', '/'))

def seller_reviews(request):
    if "log_id" not in request.session or request.session.get("log_role") != "Seller":
        return redirect("/")
        
    userid = request.session["log_id"]
    seller = registermodel.objects.get(id=userid)
    
    # Get products owned by this seller
    seller_products = product.objects.filter(sellerid=seller)
    
    # Get reviews for these products
    reviews = review.objects.filter(p_id__in=seller_products).order_by('-review_date')
    
    context = {
        "rdata": seller,
        "reviews": reviews
    }
    return render(request, "seller_reviews.html", context)


def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("Email")
        if email:
            subject = "👋 Welcome to Daily Basket Newsletter"
            message = """Dear Customer,

Thank you for subscribing to the Daily Basket Newsletter.

We’re excited to have you with us!
You will now receive:
    • Latest product updates
    • Fresh arrivals and seasonal offers
    • Exclusive discounts and deals
    • Daily Basket announcements and news

We are also happy to introduce our new feature that allows customers to schedule their orders more conveniently.

Now you can:
    • Select your preferred delivery days
    • Place weekly recurring orders
    • Schedule orders anytime from Monday to Sunday
    • Enjoy a smarter and more flexible shopping experience

Our goal is to deliver fresh products and provide a smooth, reliable, and convenient shopping experience directly to your doorstep.

Stay connected with Daily Basket for exciting updates, special rewards, and new features designed to make your daily shopping easier than ever.

Best Regards,
Daily Basket Team
Essentials Delivered Daily"""
            html_news = """
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>Newsletter — Daily Basket</title></head>
<body style="margin:0;padding:0;background:#f0f5f1;font-family:Arial,sans-serif;">
<div style="max-width:600px;margin:32px auto;border-radius:16px;overflow:hidden;box-shadow:0 8px 32px rgba(20,80,40,0.12);">
  <div style="background:#1a6b45;padding:36px 40px;text-align:center;">
    <div style="font-family:Georgia,serif;font-size:22px;color:#fff;font-weight:700;margin-bottom:4px;">
      &#128722; Daily <span style="color:#a8e6c4;">Basket</span>
    </div>
    <div style="font-size:11px;color:rgba(255,255,255,0.6);letter-spacing:1.5px;text-transform:uppercase;">Essentials Delivered Daily</div>
    <div style="font-size:42px;margin:18px 0 10px;">&#127881;</div>
    <h1 style="font-family:Georgia,serif;font-size:22px;color:#fff;font-weight:700;margin:0;">Welcome to Our Newsletter!</h1>
    <p style="color:rgba(255,255,255,0.75);font-size:13px;margin-top:6px;">You're now part of the Daily Basket family</p>
  </div>
  <div style="background:#fff;padding:32px 40px;">
    <p style="font-size:14px;color:#6b8c76;line-height:1.7;margin-bottom:20px;">
      Thank you for subscribing to the <strong style="color:#1a6b45;">Daily Basket Newsletter</strong>. 
      We're excited to have you with us!
    </p>
    <div style="font-size:13px;font-weight:600;color:#6b8c76;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;">You will now receive:</div>
    <table cellpadding="0" cellspacing="0" border="0" width="100%"
           style="border:1px solid #d4edd9;border-radius:12px;background:#f5fbf7;margin-bottom:20px;">
      <tr><td style="padding:11px 16px;border-bottom:1px solid #d4edd9;font-size:13px;color:#2d4a36;">&#127807; Latest product updates &amp; fresh arrivals</td></tr>
      <tr><td style="padding:11px 16px;border-bottom:1px solid #d4edd9;font-size:13px;color:#2d4a36;">&#127381; Seasonal offers &amp; exclusive discounts</td></tr>
      <tr><td style="padding:11px 16px;border-bottom:1px solid #d4edd9;font-size:13px;color:#2d4a36;">&#128197; Schedule your preferred delivery days</td></tr>
      <tr><td style="padding:11px 16px;font-size:13px;color:#2d4a36;">&#127881; Daily Basket announcements &amp; new features</td></tr>
    </table>
    <table cellpadding="0" cellspacing="0" border="0" width="100%"
           style="background:#1a6b45;border-radius:12px;margin-bottom:24px;">
      <tr>
        <td style="padding:16px 20px;color:rgba(255,255,255,0.8);font-size:13px;">New Feature &#10024;</td>
        <td style="padding:16px 20px;text-align:right;color:#fff;font-size:13px;font-weight:700;">Weekly Recurring Orders</td>
      </tr>
    </table>
    <p style="font-size:12px;color:#8aab94;text-align:center;line-height:1.7;">
      Stay connected for exciting updates &amp; special rewards.<br>
      This is an automated email — please do not reply directly.
    </p>
  </div>
  <div style="background:#f5fbf7;padding:24px 40px;text-align:center;border-top:1px solid #e4f0e7;">
    <div style="font-family:Georgia,serif;font-size:18px;color:#1a6b45;font-weight:700;margin-bottom:4px;">Daily <span style="color:#27ae60;">Basket</span> &#128722;</div>
    <p style="font-size:12px;color:#8aab94;">Essentials Delivered Daily &middot; Ahmedabad, Gujarat &middot; India</p>
    <div style="font-size:11px;color:#aabba8;margin-top:10px;">&copy; 2026 Daily Basket. All rights reserved.</div>
  </div>
</div>
</body></html>
            """
            news_email = EmailMultiAlternatives(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[email],
            )
            news_email.attach_alternative(html_news, "text/html")
            try:
                news_email.send(fail_silently=False)
                return HttpResponse("<script>alert('Thank you for subscribing! Check your email.'); window.location.replace(document.referrer || '/');</script>")
            except Exception as e:
                return HttpResponse(f"<script>alert('Failed to send email. Error: {str(e)}'); window.location.replace(document.referrer || '/');</script>")
    return redirect("/")

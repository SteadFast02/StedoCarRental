$(document).ready(function () 
{
    // for all product show
    $.getJSON("http://localhost:8000/api/displayvehicleinhomepage",{param:'all'}, function (data) 
    {
        // alert("XXX")
        // alert(data)
        console.log(data)
        var htm=""
        data.map((item)=>{
            htm+=`<div class="containerhover" style="margin-left: 20px; display: flex; flex-direction: column; background: white; border-radius: 15px; margin-bottom:20px;-webkit-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); -moz-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96);">
                    <div style="display: flex; justify-content: center; align-items: center;">  <img src="/${item.vehicleicon}" width="200px">  </div>
                    <div style="display: flex; justify-content: center;font-weight: bold; font-family: initial; font-size: 16px; ">${item.companyname} </div>

                    <div style="display: flex; justify-content: center;font-weight: bold; font-family: cursive; font-size: 16px; "> <b>${item.subcategoryname}</b> </div>

                    <div style="padding:1rem;">
                        <div style="display: flex;flex-direction: row;justify-content: center;">
                            <div style="display: flex; flex-direction: row;"> 
                                <span class="material-symbols-outlined">ev_station</span>
                                <span style="margin-left: 5px;"> ${item.fueltype} </span> </div>
                            <div style="display: flex; flex-direction: row;margin-left:1rem;">
                                <span class="material-symbols-outlined"> airline_seat_recline_normal </span>
                                <span style="margin-left: 5px;"> 5 Seater </span> 
                            </div>
                        </div>
                        <div style="display: flex; flex-direction: row;margin-left:1rem;justify-content: center;"> 
                                <span class="material-symbols-outlined">wb_auto</span>
                                <span> ${item.transmissiontype} </span> 
                        </div>
                        <div style="display: flex;flex-direction: row;padding: 1rem;justify-content: space-between;">
                            <div style="display: flex; align-items: flex-end;"><span class="material-symbols-outlined"> currency_rupee </span></div>
                            <div style="font-weight: bold; font-family: cursive; font-size: 1.4rem;"> ${item.price} </div>
                            <div>
                            <a href='http://localhost:8000/api/displayselectedvehicle/?vehicle=${JSON.stringify(item)}' style="text-decoration:none; cursor:pointer; color:#000" > 
                                <button style="background: linear-gradient(45deg, #007558, #97ffdd); font-weight: bold; border-radius: 5px; border: darkcyan; color:  aliceblue; height: 2.2rem; font-family: cursive; display: flex; justify-content: center; align-items: center; padding: 5px; -webkit-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); -moz-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96);">
                                    Book 
                                    <span class="material-symbols-outlined" style="font-size: small;
                                    margin-left: 10px;"> 
                                    arrow_forward_ios 
                                    </span> 
                                </button> 
                            </a>
                            </div>
                        </div>
                        <div>
                            <div>200 KMS| Prices <b>exclude</b> fuel cost</div>
                        </div> 
                    </div>
                    
                </div>`
        })
        $('#listvehicle').html(htm)
    });

    // Searching function
    function searching(value)
    {
        $.getJSON("http://localhost:8000/api/displayvehicleinhomepage",{param:value}, function (data) 
        {
            // alert("XXX")
            // alert(data)
            console.log(data)
            var htm=""
            data.map((item)=>{
            htm+=`<div class="containerhover" style="margin-left: 20px; display: flex; flex-direction: column; background: white; border-radius: 15px; margin-bottom:20px;-webkit-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); -moz-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96);">
                    <div style="display: flex; justify-content: center; align-items: center;">  <img src="/${item.vehicleicon}" width="200px">  </div>
                    <div style="display: flex; justify-content: center;font-weight: bold; font-family: initial; font-size: 16px; ">${item.companyname} </div>

                    <div style="display: flex; justify-content: center;font-weight: bold; font-family: cursive; font-size: 16px; "> <b>${item.subcategoryname}</b> </div>

                    <div style="padding:1rem;">
                        <div style="display: flex;flex-direction: row;justify-content: center;">
                            <div style="display: flex; flex-direction: row;"> 
                                <span class="material-symbols-outlined">ev_station</span>
                                <span style="margin-left: 5px;"> ${item.fueltype} </span> </div>
                            <div style="display: flex; flex-direction: row;margin-left:1rem;">
                                <span class="material-symbols-outlined"> airline_seat_recline_normal </span>
                                <span style="margin-left: 5px;"> 5 Seater </span> 
                            </div>
                        </div>
                        <div style="display: flex; flex-direction: row;margin-left:1rem;justify-content: center;"> 
                                <span class="material-symbols-outlined">wb_auto</span>
                                <span> ${item.transmissiontype} </span> 
                        </div>
                        <div style="display: flex;flex-direction: row;padding: 1rem;justify-content: space-between;">
                            <div style="display: flex; align-items: flex-end;"><span class="material-symbols-outlined"> currency_rupee </span></div>
                            <div style="font-weight: bold; font-family: cursive; font-size: 1.4rem;"> ${item.price} </div>
                            <div> 
                            <a href='http://localhost:8000/api/displayselectedvehicle/?vehicle=${JSON.stringify(item)}' style="text-decoration:none; cursor:pointer; color:#000" >
                                <button style="background: linear-gradient(45deg, #007558, #97ffdd); font-weight: bold; border-radius: 5px; border: darkcyan; color:  aliceblue; height: 2.2rem; font-family: cursive; display: flex; justify-content: center; align-items: center; padding: 5px; -webkit-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); -moz-box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96); box-shadow: 0px 8px 25px -7px rgba(0, 0, 0, 0.96);">
                                    Book 
                                    <span class="material-symbols-outlined" style="font-size: small;
                                    margin-left: 10px;"> 
                                    arrow_forward_ios 
                                    </span> 
                                </button> 
                            </a>
                            </div>
                        </div>
                        <div>
                            <div>200 KMS| Prices <b>exclude</b> fuel cost</div>
                        </div> 
                    </div>
                    
                </div>`})
                
            $('#listvehicle').html(htm)
        });
    }

    


    // Category Fetch
    $.getJSON("http://localhost:8000/api/fetchallcategory", function (data) 
    {
        // alert("XXX")
        // alert(data)
        console.log(data)
        var htm = "";
        data.map((item) => {
        htm += `          
                <div class="item containerhover">              
                    <div class="threedview">
                        <div style"border-radius:30px;width:100px;">
                            <img  src="/${item.icon}" style"border-radius:30px; width:100%;" class="threedview">
                        </div>
                        <div>
                        ${item.categoryname}
                        </div>
                    </div>
                </div>`;
        });
        $(document).ready(function() {
            var carousel = $(".carousel");
            var itemWidth = $(".item").outerWidth(true); // Include margin if any
            var visibleItems = Math.floor(carousel.parent().width() / itemWidth);
            var currentPosition = 0;

            setInterval(function() {
                if (currentPosition === (carousel.children().length - visibleItems)) {
                currentPosition = 0;
                carousel.css("transform", "translateX(0)");
                } else {
                currentPosition++;
                carousel.css("transform", "translateX(-" + (currentPosition * itemWidth) + "px)");
                }
            }, 3000); // Adjust the interval (in milliseconds) as per your preference
            });
        // console.log(htm)
        $("#catid").html(htm);

        var htm1=""
        data.map((item)=>{
            htm1+=`<div> 
            <div>
                <input class="form-check-input" type="checkbox" value=""> ${item.categoryname}
            </div>
            </div>`})
        $('#categorycheck').html(htm1)
    });

    // Subcategory Fetch
    $.getJSON("http://localhost:8000/api/fetchallsubcategory", function (data) 
    {
        // alert("XXX")
        // alert(data)
        console.log(data)
        var htm2=""
        data.map((item)=>{
            htm2+=`<div> 
            <div>
                <input class="form-check-input" type="checkbox" value=""> ${item.subcategoryname}
            </div>
            </div>`})
        $('#subcategorycheck').html(htm2)
    });

    // Brand Fetch
    $.getJSON("http://localhost:8000/api/fetchallbrand", function (data) 
    {
        // alert("XXX")
        // alert(data)
        console.log(data)
        var htm3=""
        data.map((item)=>{
            htm3+=`<div> 
            <div>
                <input class="form-check-input brand" type="checkbox" value="${item.companyname}"> ${item.companyname}
            </div>
            </div>`})
        $('#brandcheck').html(htm3)

        // searching
    $(".brand").click(function () 
    {
        var sb=''
        $(".brand").map(function (i, item) {
        
        if ($(this).prop("checked"))  
        {sb+="'"+$(this).val()+"',"}
        });
        sb=sb.substring(0,sb.length-1)
        alert(sb)
        if(sb=='')
        searching('all')
        else
        searching(sb)

    });

       
    });

    // Vehicle Count
    $.getJSON("http://localhost:8000/api/fetchvehiclecount", function (data) 
    {
        // alert("XXX")
        // alert(data)
        console.log(data)
        var htm = "";
        data.map((item) => {
        htm += `
        <div class="datetime">`;
        htm += `          
                <div class="threedview">             
                    ${item.C} Cars available for rental in Bangalore       
                </div>`;
        htm += `</div>`;
        });
        // console.log(htm)
        $("#vehiclecount").html(htm);
    });
})
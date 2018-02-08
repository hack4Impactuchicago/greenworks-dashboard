<script>
// TODO This can be moved to its own file and included with scripts.html

// Chart Globals ===============================================================
Chart.defaults.global.defaultFontFamily = "'Open Sans', 'Helvetica', sans-serif";
Chart.defaults.global.title.fontFamily = "'Montserrat', 'Helvetica', sans-serif";
Chart.defaults.global.title.fontColor = 'rgb(68, 68, 68)';
Chart.defaults.global.legend.position = 'bottom';
Chart.defaults.global.legend.padding = 15;

// Format numbers with commas in charts ========================================
Chart.scaleService.updateScaleDefaults('linear', {
	ticks: {
		callback: function (value) {
			if (value >= 1000000)
				return value / 1000000 + 'm';
			else if (value <= 999999 && value > 9999)
				return value / 1000 + 'k';
			else
			return (+value).toLocaleString();
		}
	}
})
// Format numbers with commas in tooltips ======================================
Chart.defaults.global.tooltips.callbacks.label = function (tooltipItem, data) {
	var datasetLabel = data.datasets[tooltipItem.datasetIndex].label || '';
	return datasetLabel + ': ' + (+tooltipItem.yLabel).toLocaleString();
}
</script>

<div class= "row">
  <div class="medium-16 column">
    {% capture about_content %}{% include about.md %}{% endcapture %}
    {{ about_content | markdownify }}
	</div>
	<div class="medium-8 column">
	  <aside id="secondary" class="related pll-mu">	    
        <!-- <h2>About the Application</h2> -->
	    <p>This is an open source project that uses the City of Philadelphia <a href="https://github.com/CityOfPhiladelphia/patterns">patterns</a>, <a href="http://jekyllrb.com/">Jekyll</a>, and <a href="http://www.chartjs.org/">Chart.js</a>. </p>
	    <a href="http://beta.phila.gov/feedback" class="button icon">Leave Feedback<i class="fa fa-comment"></i></a>
	    <br>
	    <a href="https://github.com/CityOfPhiladelphia/greenworks-dashboard" class="button icon">Source Code<i class="fa fa-code"></i></a>
	    <br>
	    <a href="https://www.opendataphilly.org/dataset/greenworks-dashboard" class="button icon">Download Data<i class="fa fa-table"></i></a>
        <br>
        <button id="popupbutton" class="button icon">
            Upload Data
            <i class="fa fa-cloud-upload"></i>
        </button>
	  </aside>
	</div>
</div>

<div id="myModal" class="modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <div class="form-container">
        <h2>Greenworks Dashboard: Upload Data</h2>
          <form id="CSVForm" method="post" >
              <label for="fileUpload">CSV File Upload</label>
              <div class="graphtypes">
                  <input type="file" id="fileUpload" name="firstname">
              </div>
              <label for="graph-type">Graph Type </label>
              <div class="graphtypes">
                  <input type="radio" id="graph-type" name="graphtype" value="line">Line Graph<br />
                  <input type="radio" id="graph-type" name="graphtype" value="bar">Bar Graph<br />
              </div>
              <label for="title">Title</label>
              <div class="graphtypes">
                  <input type="text" id="title" name="subject" />
              </div>
              <label for="title">Axis Titles</label>
              <div class="graphtypes">
                  X: <input type="text" id="title" name="subject" /><br/>
                  Y: <input type="text" id="title" name="subject" /><br/>
              </div>
              <label for="description">Description</label>
              <div class="graphtypes">
                  <textarea id="description" name="subject" style="height:200px"></textarea>
              </div>
            <label for="colorpickerb">Background and Border Color</label>
            <input type="checkbox" name="colorpickerb" class="default" />Check if you want default colors set.
            <div class="radioBBcwrap">
                <div class="radioBBC bbv1">
                    <input type='radio' name='colorpickerb' class='menuopt' value="">
                </div>
                <div class="radioBBC bbv2">
                    <input type='radio' name='colorpickerb' class='menuopt' value="">
                </div>
                <div class="radioBBC bbv3">
                    <input type='radio' name='colorpickerb' class='menuopt' value="">
                </div>
                <div class="radioBBC bbv4">
                    <input type='radio' name='colorpickerb' class='menuopt' value="">
                </div>
                <div class="radioBBC bbv5">
                    <input type='radio' name='colorpickerb' class='menuopt' value="">
                </div>
            </div>
            <label for="colorpicker">Color Choices</label>
            <input type="checkbox" name="colorpickerb" class="default" />Check if you want default colors set.
            <div class="radioColorThemeswrap">
                <div class="radioColor theme1">
                    <input type='radio' name='colorpicker' class='menuopt oseaside' value="seaside">
                    <!---<ul class='radioColorH Seaside'>
                        <li class="seaside t1"></li>
                        <li class="seaside t2"></li>
                        <li class="seaside t3"></li>
                        <li class="seaside t4"></li>
                        <li class="seaside t5"></li>
                    </ul>-->
                </div>
                <div class="radioColor theme2">
                    <input type='radio' name='colorpicker' class='menuopt ocrayons' value="crayons">
                    <!--<ul class='radioColorH Crayons'>
                        <li class="crayons t1"></li>
                        <li class="crayons t2"></li>
                        <li class="crayons t3"></li>
                        <li class="crayons t4"></li>
                        <li class="crayons t5"></li>
                    </ul>-->
                </div>
                <div class="radioColor theme3">
                    <input type='radio' name='colorpicker' class='menuopt onature' value="nature">
                    <!--<ul class='radioColorH Nature'>
                        <li class="nature t1"></li>
                        <li class="nature t2"></li>
                        <li class="nature t3"></li>
                        <li class="nature t4"></li>
                        <li class="nature t5"></li>
                    </ul>-->
                </div>
                <div class="radioColor theme4">
                    <input type='radio' name='colorpicker' class='menuopt ocandy' value="candy">
                    <!--<ul class='radioColorH Candy'>
                        <li class="candy t1"></li>
                        <li class="candy t2"></li>
                        <li class="candy t3"></li>
                        <li class="candy t4"></li>
                        <li class="candy t5"></li>
                    </ul>-->
                </div>
            </div>
            <input type="submit" name='Submit' class="button" value="Submit" onclick='javascript: return SubmitForm()'>
        </form>
    </div>
  </div>
</div>

<!--<script>
function SubmitForm()
{
    if(document.forms['CSVForm'].onsubmit())
    {
        document.forms['CSVForm'].action='./_includes/parse.py';
        document.forms['CSVForm'].target='_blank';
        document.forms['CSVForm'].submit();
        document.forms['CSVForm'].action={{ url_for('handle_data') }};
        document.forms['CSVForm'].target='_blank';
        document.forms['CSVForm'].submit();
    }
    return true;
}
</script>-->

<script>
    var frmvalidator = new Validator("CSVForm");
    frmvalidator.EnableOnPageErrorDisplay();
    //frmvalidator.EnableMsgsTogether();
    frmvalidator.addValidation("","req","Please provide your name");
    frmvalidator.addValidation("graphtype","req","Please provide your email address");
    frmvalidator.addValidation("message","maxlen=2048","The message is too long!(more than 2KB!)");
</script>

<script>
// Get the modal
var modal = document.getElementById('myModal');
var btn = document.getElementById("popupbutton");
var span = document.getElementsByClassName("close")[0];
// When the user clicks the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
</script>

<h2 class="ptl contrast" id="vision-1">Vision 1: Accessible Food and Drinking Water
	  <a href="#vision-1" class="header-link"><i class="fa fa-link"></i></a>
</h2>
<div class="row pbxl ptl">
  <div class="medium-16 column prxl">
    {% include charts/1-snap-participation.html %}
  </div>
  <div class="medium-8 column end">
    <aside class="related pll-mu">
      <h3 class="h4 pbl">All Philadelphians have access to healthy, affordable, and sustainable food and drinking water.</h3>
			<!-- <h4 class="h6">Note</h4> -->
			<p>Philadelphians can use <a href="http://www.fns.usda.gov/snap/supplemental-nutrition-assistance-program-snap">Supplemental Nutrition Assistance Program (SNAP)</a> benefits to purchase healthy, locally-grown food at <a href="http://thefoodtrust.org/uploads/media_items/philly-food-bucks-brochure-english.original.pdf">many farmers markets</a> citywide. Philly Food Bucks is a healthy food incentive program launched in 2010 to increase the purchasing power of SNAP customers. For every $5 that SNAP customers spend using their benefits at a participating market site, they receive a $2 Philly Food Bucks coupon for fresh fruits and vegetables.</p>

	  	<h4 class="h6">Source</h4>
	  	<p>Get Healthy Philly</p>
    </aside>
  </div>
</div>

<!-- End of each chart section with BACK TO TOP link -->
<div class="medium-24 column top">
	<a class="float-right" href="#top"><i class="fa fa-arrow-up"></i> <span class="to-top">back to top</span></a>
</div>

<h2 class="contrast" id="vision-2">Vision 2: Healthy Outdoor and Indoor Air
	<a href="#vision-2" class="header-link"><i class="fa fa-link"></i></a>
</h2>
<div class="row pbxl ptl">
  <div class="medium-16 column prxl">
    {% include charts/2-outdoor-air-quality.html %}
  </div>
  <div class="medium-8 column end">
    <aside class="related pll-mu">
      <h3 class="h4 pbl">All Philadelphians breathe healthy air inside and outside.</h3>
			<!-- <h4 class="h6">Note</h4> -->
	    <p>The <a href="http://www.phila.gov/aqi/">Air Quality Index (AQI)</a> is a daily measure of how clean or polluted our air is and how healthy it is to breathe. The Environmental Protection Agency revised the National Ambient Air Standards for ozone in 2015 and PM2.5 (particulate matter) in 2013 to hold cities and counties to higher standards for air quality. The City of Philadelphia will continue to work to meet and outperform outdoor air quality standards in the years ahead.</p>

			<h4 class="h6">Source</h4>
	  	<p>U.S. Environmental Protection Agency</p>
    </aside>
  </div>
</div>

<!-- End of each chart section with BACK TO TOP link -->
<div class="medium-24 column top">
	<a class="float-right" href="#top"><i class="fa fa-arrow-up"></i> <span class="to-top">back to top</span></a>
</div>

<h2 class="contrast" id="vision-3">Vision 3: Clean and Efficient Energy
	<a href="#vision-3" class="header-link"><i class="fa fa-link"></i></a>
</h2>
<div class="row pbxl ptl">
  <div class="medium-16 column prxl">
    {% include charts/3-citywide-energy-usage.html %}
  </div>
  <div class="medium-8 column end">
    <aside class="related pll-mu">
      <!-- <h3 class="h4 pbl">Vision</h3> -->
      <h3 class="h4 pbl">All Philadelphians efficiently use clean energy that they can afford.</h3>

			<!-- <h4 class="h6">Note</h4> -->
			<p>Annual energy use is driven in part by cold winters and hot summers that make people need to heat and cool their buildings. This demand for heating and cooling is measured in <a href="http://www.eia.gov/energyexplained/index.cfm?page=about_degree_days">degree days</a>. The extreme winters of 2010 and 2013/4 resulted in higher-than-average citywide energy use, but the 2015 decline as weather patterns stayed about the same may indicate that Philadelphia’s buildings are becoming more efficient. </p>
	  	<h4 class="h6">Source</h4>
	  	<p>City of Philadelphia Energy Office</p>
    </aside>
  </div>
</div>

<!-- End of each chart section with BACK TO TOP link -->
<div class="medium-24 column top">
	<a class="float-right" href="#top"><i class="fa fa-arrow-up"></i> <span class="to-top">back to top</span></a>
</div>

<h2 class="contrast" id="vision-4">Vision 4: Climate Prepared and Carbon Neutral Communities
	<a href="#vision-4" class="header-link"><i class="fa fa-link"></i></a>
</h2>
<div class="row pbxl ptl">
  <div class="medium-16 column prxl">
    {% include charts/4-philadelphia-carbon-footprint.html %}
  </div>
  <div class="medium-8 column end">
    <aside class="related pll-mu">
	  	<h3 class="h4 pbl">All Philadelphians are prepared for climate change and reduce carbon pollution.</h3>
	  	<!-- <h4 class="h6">Note</h4> -->
      <p>Mayor Kenney has set a goal of reducing carbon pollution 80 percent by 2050. Greenhouse gas (GHG) emissions in Philadelphia are down considerably from a 2006 baseline, but to meet our aggressive long-term target, we must increase the pace of progress. Philadelphia is developing an energy master plan for the built environment to set interim GHG reduction goals and identify policies to meet this challenge.</p>
	  	<h4 class="h6">Source</h4>
	  	<p>City of Philadelphia Energy Office</p>
    </aside>
  </div>
</div>

<!-- End of each chart section with BACK TO TOP link -->
<div class="medium-24 column top">
	<a class="float-right" href="#top"><i class="fa fa-arrow-up"></i> <span class="to-top">back to top</span></a>
</div>

<h2 class="contrast" id="vision-5">Vision 5: Quality Natural Resources
	<a href="#vision-5" class="header-link"><i class="fa fa-link"></i></a>
</h2>
<div class="row pbxl ptl">
  <div class="medium-16 column prxl">
    {% include charts/5-planted-trees.html %}
  </div>
  <div class="medium-8 column end">
    <aside class="related pll-mu">
	  	<h3 class="h4 pbl">Philadelphians benefit from  parks, trees, stormwater management, and healthy waterways.</h3>
	  	<!-- <h4 class="h6">Note</h4> -->
      <p>Philadelphians have planted more than 100,000 trees since 2009, and more than 30,000 have been planted directly by Philadelphia Parks and Recreation (PPR) or given away by PPR’s TreePhilly program for planting in private yards.</p>
	  	<h4 class="h6">Source</h4>
	  	<p>City of Philadelphia Parks and Recreation</p>
    </aside>
  </div>
</div>

<!-- End of each chart section with BACK TO TOP link -->
<div class="medium-24 column top">
	<a class="float-right" href="#top"><i class="fa fa-arrow-up"></i> <span class="to-top">back to top</span></a>
</div>

<h2 class="contrast" id="vision-6">Vision 6: Accessible, Affordable, and Safe Transportation
	<a href="#vision-6" class="header-link"><i class="fa fa-link"></i></a>
</h2>
<div class="row pbxl ptl">
  <div class="medium-16 column prxl">
    {% include charts/6-low-carbon-commute.html %}
  </div>
  <div class="medium-8 column end">
    <aside class="related pll-mu">
	  	<h3 class="h4 pbl">All Philadelphians have access to safe, affordable, and low-carbon transportation.</h3>
	  	<!-- <h4 class="h6">Note</h4> -->
      <p>Low-carbon commuting in Philadelphia has increased by more than 7,000 people in the past five years.</p>
			<p>Recent investments in pedestrian infrastructure, state funding for SEPTA improvements, and the successful launch of the Indego bike share system are improving low-carbon options to get around Philadelphia.</p>
	  	<h4 class="h6">Source</h4>
	  	<p>American Community Survey</p>
    </aside>
  </div>
</div>

<!-- End of each chart section with BACK TO TOP link -->
<div class="medium-24 column top">
	<a class="float-right" href="#top"><i class="fa fa-arrow-up"></i> <span class="to-top">back to top</span></a>
</div>

<h2 class="contrast" id="vision=7">Vision 7: Zero Waste
	<a href="#vision-7" class="header-link"><i class="fa fa-link"></i></a>
</h2>
<div class="row pbxl ptl">
  <div class="medium-16 column prxl">
    {% include charts/7-waste-diversion-rate.html %}
  </div>
  <div class="medium-8 column end">
    <aside class="related pll-mu">
	  	<h3 class="h4 pbl">All Philadelphians waste less and keep our neighborhoods clean.</h3>
		  <!-- <h4 class="h6">Note</h4> -->
	    <p>Residents, businesses, and construction in Philadelphia all produced less waste in 2014 than they did in 2007, despite an increase in population and construction. Continuing to reduce the amount we waste will make our city cleaner.</p>
	  	<h4 class="h6">Source</h4>
	  	<p>City of Philadelphia Streets Department</p>
    </aside>
  </div>
</div>

<!-- End of each chart section with BACK TO TOP link -->
<div class="medium-24 column top">
	<a class="float-right" href="#top"><i class="fa fa-arrow-up"></i> <span class="to-top">back to top</span></a>
</div>

<h2 class="contrast" id="vision-8">Vision 8: Engaged Students, Stewards, and Workers
	<a href="#vision-8" class="header-link"><i class="fa fa-link"></i></a>
</h2>
<div class="row pbxl ptl">
  <div class="medium-16 column prxl">
    {% include charts/8-engaged-philadelphians.html %}
  </div>
  <div class="medium-8 column">
    <aside class="related pll-mu">
	  	<h3 class="h4 pbl">All Philadelphians benefit from sustainability education, employment, and business opportunities.</h3>
	  	<!-- <h4 class="h6">Note</h4> -->
      <p>There are many ways Philadelphians can help make our city more sustainable, including volunteering for Philly Spring Cleanup or Waste Watchers, participating in the city’s PowerCorpsPHL job training program, or providing feedback on Greenworks, the city’s sustainability plan. For more ideas on how you can help achieve the Greenworks visons, visit <a href="www.phila.gov/green">www.phila.gov/green</a> to see our new Greenworks on the Ground checklists.</p>
	  	<h4 class="h6">Source</h4>
	  	<p>City of Philadelphia Office of Sustainability and Partners</p>
    </aside>
  </div>
</div>

<!-- End of each chart section with BACK TO TOP link -->
<div class="medium-24 column top">
	<a class="float-right" href="#top"><i class="fa fa-arrow-up"></i> <span class="to-top">back to top</span></a>
</div>

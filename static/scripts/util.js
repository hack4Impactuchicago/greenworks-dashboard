function pluck (rows, key) {
  return rows.map(function (row) {
    return row[key]
  })
}

function getScriptParent () {
  var scriptEls = document.querySelectorAll('script')
  var thisScriptEl = scriptEls[scriptEls.length - 1]
  return thisScriptEl.parentNode
}

// TODO This can be moved to its own file and included with scripts.html

// Chart Globals ===============================================================
Chart.defaults.global.defaultFontFamily = "'Open Sans', 'Helvetica', sans-serif";
Chart.defaults.global.title.fontFamily = "'Montserrat', 'Helvetica', sans-serif";
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

// Can we handle some of the numeric formatting here?
// (Locale, rounding for sets in millions?)

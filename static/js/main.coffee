class @Header
	constructor: (@glued) ->
		@switchGlue()

		$("#set-header").click () => 
			@switchGlue()
			@updateDatabaseGlue()

	switchGlue: () ->
		if @glued
			@unglue()
		else @glue()
		
	updateDatabaseGlue: () ->
		$.ajax
			url:  "/users/glue",
			type: "POST",
			data: "glued=" + (@glued + 0)

	### Glue the header to the top of the page ###
	glue: () -> 
		@glued=true
		
		headerCSS = 
			"position":"absolute"

		$("#header").css headerCSS

		$("#set-header").html "↓"

	### Unglue the header from the top of the page ###
	unglue: () -> 
		@glued=false
		headerCSS = 
			"position":"fixed"

		$("#header").css headerCSS

		$("#set-header").html "↑"

class @Notice
	constructor: (@title,@content) ->
		$("#notice").slideDown "slow"
		
		$("#notice").html "<span class='close'></span><h4>" + @title + "</h4><p>" + @content + "</p>"

		$("#notice .close").click @die

	die: () ->
		$("#notice").slideUp "fast", () =>
			$("#notice").hide()

class @Modal
	constructor: (@modalDiv) ->
		$("#modal .close").click @die
		
		@show()

	show: () ->
		@visible=true
		$(@modalDiv).css("display","block")
		$("#modal").css("display","block")

	die: () ->
		@visible=false
		$("#modal aside").css("display","none")
		$("#modal").css("display","none")

class @Helpbox
	constructor: (@helpDiv) ->
		$(@helpDiv).click @die

		$(@helpDiv).addClass "helpBox"
		$(@helpDiv).addClass "roundBox"

		@show()

	show: () ->
		$(@helpDiv).css "display","block"

	die: () =>
		$(@helpDiv).css "display","none"

$(document).ready ->
	### Keeps the copyright up to date on the current year ###
	date = new Date()
	$("#copyright-date").html date.getFullYear()

	### Set up the header ###
	header = new Header false
	if $("#glued").attr("data-glued") == "0"
		header.switchGlue()

	### Flashed Messages ###
	$("#flashed li").each ->
		new Notice "MESSAGE" ,$(this).text()

	### Registration ###		
	Recaptcha.create $("#registerCaptcha").attr("data-publicKey"), "registerCaptcha", theme : 'custom', custom_theme_widget: 'recaptcha_widget', callback: Recaptcha.focus_response_field
	$("#register-button").click () =>
		signupModal = new Modal "#register-form"
		$('form:not(.filter) :input:visible:first').focus()

	$("#register-form form").submit () =>
		form = $("#register-form form").serialize()
		$.ajax
			url:  "/users/signup",
			type: "POST",
			data: form,
			success: (data) =>
				if data == "1"
					window.location = "/users/welcome"
		false

	### Login ###
	$("#login-button").click () =>
		loginModal = new Modal "#login-form"
		$('form:not(.filter) :input:visible:first').focus()
		
	$("#login-form form").submit () =>
		form = $("#login-form form").serialize()
		$.ajax
			url:  "/users/login",
			type: "POST",
			data: form,
			success: (data) =>
				if data == "1"
					location.reload true
				if data == "0"
					new Notice "Woops!", "Incorrect Username/Password combination. Remember that your password is case sensative! "
		false

	### Logout ###
	$("#logout-button").click () =>
		$.ajax
			url:  "/users/logout",
			type: "POST",
			success: (data) =>
				if data == "1"
					window.location = "/"

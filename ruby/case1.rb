puts "start"

require 'rubygems'
require 'appium_lib'

APP_PATH = 'D:/Appium-project/apk/P01_AndroidApp.2.apk'

desired_caps = {
  caps:       {
    platformName:  'Android',
    versionNumber: '4.2.2',
    deviceName:    'emulator-5554',
    app:           APP_PATH,
  },
  appium_lib: {
    sauce_username:   nil, # don't run on Sauce
    sauce_access_key: nil
  }
}

# Start the driver
Appium::Driver.new(desired_caps).start_driver



module AndroidApp
  module Android
    # Add all the Appium library methods to Test to make
    # calling them look nicer.
    Appium.promote_singleton_appium_methods AndroidApp


	
	puts 'start to click hello world button'
	#button('Hello World, Click Me!').click
	find('Hello World, Click Me!').click
	find('1 clicks!').click
	find('Click to login page').click
	puts 'end click hello world button'

	objName = textfield 1
	objName.send_keys 'hello'
	
	objPsw = textfield 2
	objPsw.send_keys 'abc'
	
	
	puts 'start to click back key'
	puts first_text.text
	puts 'end click back key'
	
	
	#button(1).click
	button('Login').click
	
	puts 'start to sleep'
	sleep(3)
	puts 'end sleep'
	
	
	ele = find '2131034121' #get element you want
	execute_script "mobile: scrollTo", :direction => 'right', :element => ele.ref
	
	
    # Quit when you're done!
	puts 'start to driver_quite'
    driver_quit
	puts 'end driver_quit'
	
    puts 'Tests Succeeded!'
  end
end

puts "the end"
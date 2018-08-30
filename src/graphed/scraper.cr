require "halite"
require "./info"

module Graphed

  URL = "https://hac.friscoisd.org/HomeAccess"

  # Scraper will log into HAC, scrape grades, and return a Grades object
  class Scraper
    def initalize()
      @client = Halite::Client.new
    end

    # log in
    private def login(username, password)
      @client.post(URL + "/Account/LogOn", form: { "LogOnDetails.UserName" => username, "LogOnDetails.Password" => password })
    end

    # scrape grades and return Grades
    def getGrades(username, password)
      login(username, password)
    end
  end
end

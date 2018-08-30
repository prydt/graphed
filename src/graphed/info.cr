require "json"

module Graphed

  # Courses contain grades and an average grade
  class Course
    JSON.mapping(
      # assignment name => grade
      grades: Hash(String, Float64),
      average: Float64,
    )
  end

  # Grades is the total of all classes in an array
  class Grades
    JSON.mapping(
      classes: Array(Course)
    )
  end

end

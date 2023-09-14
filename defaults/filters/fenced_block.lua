function Div(el)
  if el.classes[1] == "note" then
    -- insert element in front
    if el.attributes.title then
      st = "\\begin{Note}{"..el.attributes.title.."}"
    else 
      st = "\\begin{Note}"
    end
    table.insert(
      el.content, 1,
      pandoc.RawBlock("latex", st))
    -- insert element at the back
    table.insert(
      el.content,
      pandoc.RawBlock("latex", "\\end{Note}"))
  end
  return el
end
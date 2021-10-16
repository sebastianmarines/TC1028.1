Mix.install([
  {:httpoison, "~> 1.8"},
  {:floki, "~> 0.31.0"}
])

defmodule Words do
  def get(loops) do
    get([], loops)
  end

  defp get(word_list, loops) do
    if loops == 0 do
      word_list
    else
      Process.sleep(700)
      IO.write(".")

      scrape_word(word_list)
      |> get(loops - 1)
    end
  end

  defp scrape_word(word_list) do
    resp = request("https://www.palabrasque.com/palabra-aleatoria.php?Submit=Nueva+palabra")

    word =
      resp
      |> Floki.parse_document!()
      |> Floki.find("b")
      |> Enum.at(0)
      |> elem(2)
      |> Enum.at(0)
      |> :unicode.characters_to_nfd_binary()
      |> String.replace(~r/\W/u, "")
      |> String.upcase()

    [word | word_list]
  end

  defp request(url) do
    case HTTPoison.get(url) do
      {:ok, %HTTPoison.Response{status_code: 200, body: body}} ->
        body

      {:error, %HTTPoison.Error{}} ->
        IO.write("!")
        Process.sleep(10000)
        request(url)
    end
  end
end

[number_arg] = System.argv()

{number, _} = Integer.parse(number_arg)

IO.puts("Starting...")

words_list = Words.get(number)

File.write!("palabras.txt", Enum.join(words_list, "\n"))

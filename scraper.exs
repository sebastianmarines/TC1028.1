Mix.install([
  {:httpoison, "~> 1.8"},
  {:floki, "~> 0.31.0"}
])

defmodule Words do
  def get(loops) do
    get([], loops)
  end

  defp get(word_list, 0) do
    word_list
  end

  defp get(word_list, loops) do
    Process.sleep(50)
    IO.write(".")

    scrape_word(word_list)
    |> get(loops - 1)
  end

  defp scrape_word(word_list) do
    request("https://www.palabrasque.com/palabra-aleatoria.php?Submit=Nueva+palabra")
    |> Floki.parse_document!()
    |> Floki.find("b")
    |> Enum.at(0)
    |> elem(2)
    |> Enum.at(0)
    |> :unicode.characters_to_nfd_binary()
    |> String.replace(~r/\W/u, "")
    |> String.upcase()
    |> (&[&1 | word_list]).()
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

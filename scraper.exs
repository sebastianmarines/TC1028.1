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
      if rem(loops, 10) == 0 do
        :timer.sleep(2)
      end

      scrape_word(word_list)
      |> get(loops - 1)
    end
  end

  defp scrape_word(word_list) do
    resp = HTTPoison.get!("https://www.aleatorios.com/")

    word =
      resp.body
      |> Floki.parse_document!()
      |> Floki.find("div.col.text-center.result")
      |> Floki.find("h1")
      |> Enum.at(0)
      |> elem(2)
      |> Enum.at(0)
      |> String.split("\n")
      |> Enum.at(0)
      |> :unicode.characters_to_nfd_binary()
      |> String.replace(~r/\W/u, "")

    [word | word_list]
  end
end

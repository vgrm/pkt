// Valdas Germanauskas IFF-6/14
// 750 - 8 Queens Chess Problem 

open System
open System.IO

let rec iterate f value = seq { 
    yield value
    yield! iterate f (f value) }
 
 //directions
let up i = i + 1
let right i = i
let down i = i - 1

let noCollisionGivenDir solution number dir =
    Seq.forall2 (<>) solution (Seq.skip 1 (iterate dir number))
 
let goodAddition solution number =
    List.forall (noCollisionGivenDir solution number) [ up; right; down ]
 
let extendSolution ps =
    [1..8]
    |> List.filter (goodAddition ps)
    |> List.map (fun num -> num :: ps)
 
let allSolutions =
    iterate (List.collect (extendSolution)) [[]]
 
//get solutions for the 8x8 chessboard where a queen is given at col and row
let findSolutions (col : int, row : int) =
    allSolutions
    |> Seq.item 8
    |> Seq.filter (fun x -> x.Item(col-1).Equals(row))

let print items =
    use file = System.IO.File.AppendText("temp.txt")
    items 
    |> Seq.iter (fprintf file "%A")
    fprintfn file ""

[<EntryPoint>]
let main argv =

    printfn "Enter x coordinate and then the y coordinate"
    //get x and y coords of the first queen
    let xCoord = Console.ReadLine();
    let yCoord = Console.ReadLine();

    let results = findSolutions(Convert.ToInt32(xCoord), Convert.ToInt32(yCoord))

    use file = System.IO.File.CreateText("temp.txt")
    fprintfn file "SOLN#"

    file.Close()
    results
    |> Seq.iter print

    0;;

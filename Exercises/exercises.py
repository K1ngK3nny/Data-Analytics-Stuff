Sub WellsFargo_PT1

    For Each ws In Worksheets
      Dim WorksheetName as String
      LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
      WorksheetName = ws.name
      State = Split(WorksheetName, "_")
      ws.Range("A1").EntireColumn.Insert
      ws.Cells(1,1).Value = "State"
      ws.Range("A2:A" & LastRow) = State(0)
      LastColumn = ws.Cells(1, Columns.Count).End(xlToLeft).Column
      For i = 3 To LastColumn
        YearHeader = ws.Cells(1, i).Value
        YearSplit = Split(YearHeader, " ")
        ws.Cells(1, i).Value = YearSplit(3)
      Next i 

      For i = 2 To LastRow
        For j = 2 To LastColumn
          ws.Cells(i, j).Style = "Currency"
        Next j
      Next i
    
    Next ws
    MsgBox ("Fixes Complete")
End Sub


import main


def test_main_runs(capsys):
    main.main()

    captured = capsys.readouterr()

    assert "Original Dataset" in captured.out
    assert "Applying Encryption Strategy" in captured.out
    assert "Applying Compression Strategy" in captured.out
